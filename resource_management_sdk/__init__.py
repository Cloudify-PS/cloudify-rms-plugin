from context import ResourceManagementContext

from handle import (
    ProjectHandler,
    GlobalQuotaHandler,
    ProjectQuotaHandler,
    GlobalUsageHandler,
    ProjectUsageHandler
)

DEFAULT_HANDLER_CHAIN = (
    ProjectHandler,
    GlobalQuotaHandler,
    ProjectQuotaHandler,
    GlobalUsageHandler,
    ProjectUsageHandler
)


class Engine(object):

    @classmethod
    def _prepare_resource_management_context(cls, ctx):
        return ResourceManagementContext(ctx)

    def __init__(self, logger, rest_client, handlers):
        self.logger = logger
        self.rest_client = rest_client
        self.handlers = [handler_cls(logger) for handler_cls in handlers]

    def _collect_data(self, rsm_ctx):
        while True:
            for handler in self.handlers:
                if handler.can_handle(rsm_ctx):
                    handler.handle(rsm_ctx)
                    break

            if not rsm_ctx.next_instance():
                break

        for k, v in rsm_ctx.collected_data.iteritems():
            self.logger.info('RESOURCE: {} -- {}'.format(k, v))

    def run(self, ctx):
        rsm_ctx = self._prepare_resource_management_context(ctx)
        self._collect_data(rsm_ctx)


def get_handlers():
    return DEFAULT_HANDLER_CHAIN

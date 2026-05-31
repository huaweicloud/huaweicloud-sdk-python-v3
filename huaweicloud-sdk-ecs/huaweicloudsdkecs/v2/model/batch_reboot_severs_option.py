# coding: utf-8
import warnings

from .batch_reboot_servers_option import BatchRebootServersOption


class BatchRebootSeversOption(BatchRebootServersOption):
    """
    Deprecated: This class contains a typo.
    Please use BatchRebootServersOption instead.
    """
    def __init__(self, *args, **kwargs):
        # 在初始化时发出弃用警告，提示开发者使用新类
        warnings.warn(
            "BatchRebootSeversOption is deprecated and contains a typo. "
            "Please use BatchRebootServersOption instead.",
            DeprecationWarning,
            stacklevel=2
        )
        super().__init__(*args, **kwargs)

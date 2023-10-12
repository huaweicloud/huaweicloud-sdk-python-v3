# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppServerTaskStatus:
    """
    allowed enum values
    """
    SCHEDULING = "scheduling"
    BLOCK_DEVICE_MAPPING = "block_device_mapping"
    NETWORKING = "networking"
    SPAWNING = "spawning"
    REBOOTING = "rebooting"
    REBOOT_PENDING = "reboot_pending"
    REBOOTING_HARD = "rebooting_hard"
    REBOOT_PENDING_HARD = "reboot_pending_hard"
    REBOOT_STARTED_HARD = "reboot_started_hard"
    REBUILDING = "rebuilding"
    REBUILD_FAIL = "rebuild_fail"
    UPDATING_TSVI = "updating_tsvi"
    UPDATING_TSVI_FAILED = "updating_tsvi_failed"
    REBUILD_BLOCK_DEVICE_MAPPING = "rebuild_block_device_mapping"
    REBUILD_SPAWNING = "rebuild_spawning"
    MIGRATING = "migrating"
    RESIZE_PREP = "resize_prep"
    RESIZE_MIGRATING = "resize_migrating"
    RESIZE_MIGRATED = "resize_migrated"
    RESIZE_FINISH = "resize_finish"
    RESIZE_REVERTING = "resize_reverting"
    POWERING_OFF = "powering-off"
    POWERING_ON = "powering-on"
    DELETING = "deleting"
    REJOINING_DOMAIN = "rejoining_domain"
    SOURCE_LOCKING = "source_locking"
    DELETE_FAILED = "delete_failed"
    UPDATING_SID = "updating_sid"
    UPGRADING_ACCESS_AGENT = "upgrading_access_agent"
    UPGRAD_ACCESS_AGENT_FAIL = "upgrad_access_agent_fail"
    UPGRAD_ACCESS_AGENT_SUCCESS = "upgrad_access_agent_success"
    MIGRATE_FAILED = "migrate_failed"
    BUILD_IMAGE = "build_image"
    NULL = "null"
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self):
        """AppServerTaskStatus

        The model defined in huaweicloud sdk

        """
        
        
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AppServerTaskStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobType:
    """
    allowed enum values
    """
    CREATE_SERVER = "CREATE_SERVER"
    DELETE_SERVER = "DELETE_SERVER"
    UPDATE_FREEZE_STATUS = "UPDATE_FREEZE_STATUS"
    CREATE_SERVER_IMAGE = "CREATE_SERVER_IMAGE"
    REINSTALL_OS = "REINSTALL_OS"
    CHANGE_SERVER_IMAGE = "CHANGE_SERVER_IMAGE"
    REJOIN_DOMAIN = "REJOIN_DOMAIN"
    MIGRATE_SERVER = "MIGRATE_SERVER"
    UPGRADE_ACCESS_AGENT = "UPGRADE_ACCESS_AGENT"
    UPDATE_SERVER_TSVI = "UPDATE_SERVER_TSVI"
    SCHEDULED_TASK = "SCHEDULED_TASK"
    COLLECT_HDA_LOG = "COLLECT_HDA_LOG"
    COLLECT_APS_LOG = "COLLECT_APS_LOG"
    CREATE_SERVER_SNAPSHOT = "CREATE_SERVER_SNAPSHOT"
    DELETE_SERVER_SNAPSHOT = "DELETE_SERVER_SNAPSHOT"
    RESTORE_SERVER_SNAPSHOT = "RESTORE_SERVER_SNAPSHOT"
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
        r"""JobType

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
        if not isinstance(other, JobType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

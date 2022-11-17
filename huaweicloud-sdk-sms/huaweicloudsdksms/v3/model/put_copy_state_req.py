# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutCopyStateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'copystate': 'str',
        'migrationcycle': 'str'
    }

    attribute_map = {
        'copystate': 'copystate',
        'migrationcycle': 'migrationcycle'
    }

    def __init__(self, copystate=None, migrationcycle=None):
        """PutCopyStateReq

        The model defined in huaweicloud sdk

        :param copystate: 源端服务器状 UNAVAILABLE：环境校验不通过 WAITING：等待 INIT：初始化 REPLICATE：复制 SYNCING：持续同步 STOPPING：暂停中 STOPPED：已暂停 DELETING：删除中 ERROR：错误 CLONING：等待克隆完成 CUTOVERING：启动目的端中 FINISHED：启动目的端完成
        :type copystate: str
        :param migrationcycle: 迁移周期 cutovering:启动目的端中 cutovered:启动目的端完成 checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 
        :type migrationcycle: str
        """
        
        

        self._copystate = None
        self._migrationcycle = None
        self.discriminator = None

        if copystate is not None:
            self.copystate = copystate
        if migrationcycle is not None:
            self.migrationcycle = migrationcycle

    @property
    def copystate(self):
        """Gets the copystate of this PutCopyStateReq.

        源端服务器状 UNAVAILABLE：环境校验不通过 WAITING：等待 INIT：初始化 REPLICATE：复制 SYNCING：持续同步 STOPPING：暂停中 STOPPED：已暂停 DELETING：删除中 ERROR：错误 CLONING：等待克隆完成 CUTOVERING：启动目的端中 FINISHED：启动目的端完成

        :return: The copystate of this PutCopyStateReq.
        :rtype: str
        """
        return self._copystate

    @copystate.setter
    def copystate(self, copystate):
        """Sets the copystate of this PutCopyStateReq.

        源端服务器状 UNAVAILABLE：环境校验不通过 WAITING：等待 INIT：初始化 REPLICATE：复制 SYNCING：持续同步 STOPPING：暂停中 STOPPED：已暂停 DELETING：删除中 ERROR：错误 CLONING：等待克隆完成 CUTOVERING：启动目的端中 FINISHED：启动目的端完成

        :param copystate: The copystate of this PutCopyStateReq.
        :type copystate: str
        """
        self._copystate = copystate

    @property
    def migrationcycle(self):
        """Gets the migrationcycle of this PutCopyStateReq.

        迁移周期 cutovering:启动目的端中 cutovered:启动目的端完成 checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 

        :return: The migrationcycle of this PutCopyStateReq.
        :rtype: str
        """
        return self._migrationcycle

    @migrationcycle.setter
    def migrationcycle(self, migrationcycle):
        """Sets the migrationcycle of this PutCopyStateReq.

        迁移周期 cutovering:启动目的端中 cutovered:启动目的端完成 checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 

        :param migrationcycle: The migrationcycle of this PutCopyStateReq.
        :type migrationcycle: str
        """
        self._migrationcycle = migrationcycle

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
        if not isinstance(other, PutCopyStateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

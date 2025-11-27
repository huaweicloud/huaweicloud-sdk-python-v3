# coding: utf-8

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
        r"""PutCopyStateReq

        The model defined in huaweicloud sdk

        :param copystate: 源端服务器状态 unavailable：环境校验不通过 waiting：等待 initialize：初始化 replicate：复制 syncing：持续同步 stopping：暂停中 stopped：已暂停 skipping：跳过中 deleting：删除中 clearing: 清理快照资源中 cleared：清理快照资源完成 clearfailed：清理快照资源失败 premigready：迁移演练就绪 premiged：迁移演练完成 premigfailed：迁移演练失败 cloning：等待克隆完成 cutovering：启动目的端中 finished：启动目的端完成 error：错误
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
        r"""Gets the copystate of this PutCopyStateReq.

        源端服务器状态 unavailable：环境校验不通过 waiting：等待 initialize：初始化 replicate：复制 syncing：持续同步 stopping：暂停中 stopped：已暂停 skipping：跳过中 deleting：删除中 clearing: 清理快照资源中 cleared：清理快照资源完成 clearfailed：清理快照资源失败 premigready：迁移演练就绪 premiged：迁移演练完成 premigfailed：迁移演练失败 cloning：等待克隆完成 cutovering：启动目的端中 finished：启动目的端完成 error：错误

        :return: The copystate of this PutCopyStateReq.
        :rtype: str
        """
        return self._copystate

    @copystate.setter
    def copystate(self, copystate):
        r"""Sets the copystate of this PutCopyStateReq.

        源端服务器状态 unavailable：环境校验不通过 waiting：等待 initialize：初始化 replicate：复制 syncing：持续同步 stopping：暂停中 stopped：已暂停 skipping：跳过中 deleting：删除中 clearing: 清理快照资源中 cleared：清理快照资源完成 clearfailed：清理快照资源失败 premigready：迁移演练就绪 premiged：迁移演练完成 premigfailed：迁移演练失败 cloning：等待克隆完成 cutovering：启动目的端中 finished：启动目的端完成 error：错误

        :param copystate: The copystate of this PutCopyStateReq.
        :type copystate: str
        """
        self._copystate = copystate

    @property
    def migrationcycle(self):
        r"""Gets the migrationcycle of this PutCopyStateReq.

        迁移周期 cutovering:启动目的端中 cutovered:启动目的端完成 checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 

        :return: The migrationcycle of this PutCopyStateReq.
        :rtype: str
        """
        return self._migrationcycle

    @migrationcycle.setter
    def migrationcycle(self, migrationcycle):
        r"""Sets the migrationcycle of this PutCopyStateReq.

        迁移周期 cutovering:启动目的端中 cutovered:启动目的端完成 checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 

        :param migrationcycle: The migrationcycle of this PutCopyStateReq.
        :type migrationcycle: str
        """
        self._migrationcycle = migrationcycle

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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

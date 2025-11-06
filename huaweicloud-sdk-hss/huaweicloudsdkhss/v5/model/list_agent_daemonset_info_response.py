# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgentDaemonsetInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_list': 'list[ClusterInfoResponse]',
        'total_num': 'int',
        'upgradeful_num': 'int',
        'err_running_num': 'int',
        'err_access_num': 'int'
    }

    attribute_map = {
        'data_list': 'data_list',
        'total_num': 'total_num',
        'upgradeful_num': 'upgradeful_num',
        'err_running_num': 'err_running_num',
        'err_access_num': 'err_access_num'
    }

    def __init__(self, data_list=None, total_num=None, upgradeful_num=None, err_running_num=None, err_access_num=None):
        r"""ListAgentDaemonsetInfoResponse

        The model defined in huaweicloud sdk

        :param data_list: **参数解释**: 数据列表 **取值范围**: 取值0-200 
        :type data_list: list[:class:`huaweicloudsdkhss.v5.ClusterInfoResponse`]
        :param total_num: **参数解释** 已接入集群总数 **取值范围** 取值0-65535
        :type total_num: int
        :param upgradeful_num: **参数解释** 待升级集群总数 **取值范围** 取值0-65535
        :type upgradeful_num: int
        :param err_running_num: **参数解释** 运行异常集群总数 **取值范围** 取值0-65535
        :type err_running_num: int
        :param err_access_num: **参数解释** 接入异常集群总数 **取值范围** 取值0-65535
        :type err_access_num: int
        """
        
        super().__init__()

        self._data_list = None
        self._total_num = None
        self._upgradeful_num = None
        self._err_running_num = None
        self._err_access_num = None
        self.discriminator = None

        if data_list is not None:
            self.data_list = data_list
        if total_num is not None:
            self.total_num = total_num
        if upgradeful_num is not None:
            self.upgradeful_num = upgradeful_num
        if err_running_num is not None:
            self.err_running_num = err_running_num
        if err_access_num is not None:
            self.err_access_num = err_access_num

    @property
    def data_list(self):
        r"""Gets the data_list of this ListAgentDaemonsetInfoResponse.

        **参数解释**: 数据列表 **取值范围**: 取值0-200 

        :return: The data_list of this ListAgentDaemonsetInfoResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ClusterInfoResponse`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ListAgentDaemonsetInfoResponse.

        **参数解释**: 数据列表 **取值范围**: 取值0-200 

        :param data_list: The data_list of this ListAgentDaemonsetInfoResponse.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.ClusterInfoResponse`]
        """
        self._data_list = data_list

    @property
    def total_num(self):
        r"""Gets the total_num of this ListAgentDaemonsetInfoResponse.

        **参数解释** 已接入集群总数 **取值范围** 取值0-65535

        :return: The total_num of this ListAgentDaemonsetInfoResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListAgentDaemonsetInfoResponse.

        **参数解释** 已接入集群总数 **取值范围** 取值0-65535

        :param total_num: The total_num of this ListAgentDaemonsetInfoResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def upgradeful_num(self):
        r"""Gets the upgradeful_num of this ListAgentDaemonsetInfoResponse.

        **参数解释** 待升级集群总数 **取值范围** 取值0-65535

        :return: The upgradeful_num of this ListAgentDaemonsetInfoResponse.
        :rtype: int
        """
        return self._upgradeful_num

    @upgradeful_num.setter
    def upgradeful_num(self, upgradeful_num):
        r"""Sets the upgradeful_num of this ListAgentDaemonsetInfoResponse.

        **参数解释** 待升级集群总数 **取值范围** 取值0-65535

        :param upgradeful_num: The upgradeful_num of this ListAgentDaemonsetInfoResponse.
        :type upgradeful_num: int
        """
        self._upgradeful_num = upgradeful_num

    @property
    def err_running_num(self):
        r"""Gets the err_running_num of this ListAgentDaemonsetInfoResponse.

        **参数解释** 运行异常集群总数 **取值范围** 取值0-65535

        :return: The err_running_num of this ListAgentDaemonsetInfoResponse.
        :rtype: int
        """
        return self._err_running_num

    @err_running_num.setter
    def err_running_num(self, err_running_num):
        r"""Sets the err_running_num of this ListAgentDaemonsetInfoResponse.

        **参数解释** 运行异常集群总数 **取值范围** 取值0-65535

        :param err_running_num: The err_running_num of this ListAgentDaemonsetInfoResponse.
        :type err_running_num: int
        """
        self._err_running_num = err_running_num

    @property
    def err_access_num(self):
        r"""Gets the err_access_num of this ListAgentDaemonsetInfoResponse.

        **参数解释** 接入异常集群总数 **取值范围** 取值0-65535

        :return: The err_access_num of this ListAgentDaemonsetInfoResponse.
        :rtype: int
        """
        return self._err_access_num

    @err_access_num.setter
    def err_access_num(self, err_access_num):
        r"""Sets the err_access_num of this ListAgentDaemonsetInfoResponse.

        **参数解释** 接入异常集群总数 **取值范围** 取值0-65535

        :param err_access_num: The err_access_num of this ListAgentDaemonsetInfoResponse.
        :type err_access_num: int
        """
        self._err_access_num = err_access_num

    def to_dict(self):
        import warnings
        warnings.warn("ListAgentDaemonsetInfoResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListAgentDaemonsetInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnableClusterGroupPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'clustergroupid': 'str',
        'retry': 'str'
    }

    attribute_map = {
        'clustergroupid': 'clustergroupid',
        'retry': 'retry'
    }

    def __init__(self, clustergroupid=None, retry=None):
        r"""EnableClusterGroupPolicyRequest

        The model defined in huaweicloud sdk

        :param clustergroupid: 容器舰队id
        :type clustergroupid: str
        :param retry: 重试启动策略管理功能
        :type retry: str
        """
        
        

        self._clustergroupid = None
        self._retry = None
        self.discriminator = None

        self.clustergroupid = clustergroupid
        if retry is not None:
            self.retry = retry

    @property
    def clustergroupid(self):
        r"""Gets the clustergroupid of this EnableClusterGroupPolicyRequest.

        容器舰队id

        :return: The clustergroupid of this EnableClusterGroupPolicyRequest.
        :rtype: str
        """
        return self._clustergroupid

    @clustergroupid.setter
    def clustergroupid(self, clustergroupid):
        r"""Sets the clustergroupid of this EnableClusterGroupPolicyRequest.

        容器舰队id

        :param clustergroupid: The clustergroupid of this EnableClusterGroupPolicyRequest.
        :type clustergroupid: str
        """
        self._clustergroupid = clustergroupid

    @property
    def retry(self):
        r"""Gets the retry of this EnableClusterGroupPolicyRequest.

        重试启动策略管理功能

        :return: The retry of this EnableClusterGroupPolicyRequest.
        :rtype: str
        """
        return self._retry

    @retry.setter
    def retry(self, retry):
        r"""Sets the retry of this EnableClusterGroupPolicyRequest.

        重试启动策略管理功能

        :param retry: The retry of this EnableClusterGroupPolicyRequest.
        :type retry: str
        """
        self._retry = retry

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
        if not isinstance(other, EnableClusterGroupPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

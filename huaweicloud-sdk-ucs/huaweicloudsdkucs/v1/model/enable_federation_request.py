# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnableFederationRequest:

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
        'retryjoinall': 'bool'
    }

    attribute_map = {
        'clustergroupid': 'clustergroupid',
        'retryjoinall': 'retryjoinall'
    }

    def __init__(self, clustergroupid=None, retryjoinall=None):
        r"""EnableFederationRequest

        The model defined in huaweicloud sdk

        :param clustergroupid: 容器舰队id
        :type clustergroupid: str
        :param retryjoinall: 是否重试集群加入联邦
        :type retryjoinall: bool
        """
        
        

        self._clustergroupid = None
        self._retryjoinall = None
        self.discriminator = None

        self.clustergroupid = clustergroupid
        if retryjoinall is not None:
            self.retryjoinall = retryjoinall

    @property
    def clustergroupid(self):
        r"""Gets the clustergroupid of this EnableFederationRequest.

        容器舰队id

        :return: The clustergroupid of this EnableFederationRequest.
        :rtype: str
        """
        return self._clustergroupid

    @clustergroupid.setter
    def clustergroupid(self, clustergroupid):
        r"""Sets the clustergroupid of this EnableFederationRequest.

        容器舰队id

        :param clustergroupid: The clustergroupid of this EnableFederationRequest.
        :type clustergroupid: str
        """
        self._clustergroupid = clustergroupid

    @property
    def retryjoinall(self):
        r"""Gets the retryjoinall of this EnableFederationRequest.

        是否重试集群加入联邦

        :return: The retryjoinall of this EnableFederationRequest.
        :rtype: bool
        """
        return self._retryjoinall

    @retryjoinall.setter
    def retryjoinall(self, retryjoinall):
        r"""Sets the retryjoinall of this EnableFederationRequest.

        是否重试集群加入联邦

        :param retryjoinall: The retryjoinall of this EnableFederationRequest.
        :type retryjoinall: bool
        """
        self._retryjoinall = retryjoinall

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
        if not isinstance(other, EnableFederationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

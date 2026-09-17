# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateResourceBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'action': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'action': 'action'
    }

    def __init__(self, cluster_id=None, action=None):
        r"""UpdateResourceBody

        The model defined in huaweicloud sdk

        :param cluster_id: 需要更改绑定的集群id。
        :type cluster_id: str
        :param action: 操作类型, 绑定:bind、解绑:unbind。
        :type action: str
        """
        
        

        self._cluster_id = None
        self._action = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.action = action

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this UpdateResourceBody.

        需要更改绑定的集群id。

        :return: The cluster_id of this UpdateResourceBody.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this UpdateResourceBody.

        需要更改绑定的集群id。

        :param cluster_id: The cluster_id of this UpdateResourceBody.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def action(self):
        r"""Gets the action of this UpdateResourceBody.

        操作类型, 绑定:bind、解绑:unbind。

        :return: The action of this UpdateResourceBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this UpdateResourceBody.

        操作类型, 绑定:bind、解绑:unbind。

        :param action: The action of this UpdateResourceBody.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, UpdateResourceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

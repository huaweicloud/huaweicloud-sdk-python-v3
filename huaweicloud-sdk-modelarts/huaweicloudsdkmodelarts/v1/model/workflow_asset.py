# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowAsset:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'content_id': 'str',
        'subscription_id': 'str',
        'expired_at': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'content_id': 'content_id',
        'subscription_id': 'subscription_id',
        'expired_at': 'expired_at'
    }

    def __init__(self, name=None, type=None, content_id=None, subscription_id=None, expired_at=None):
        r"""WorkflowAsset

        The model defined in huaweicloud sdk

        :param name: 资产名称。
        :type name: str
        :param type: 资产类型，枚举如下: - algorithm：算法 - algorithm2：新算法 - model：模型算法
        :type type: str
        :param content_id: 资产ID，可在AI Gallery中获取。
        :type content_id: str
        :param subscription_id: 订阅ID，可在AI Gallery中获取。
        :type subscription_id: str
        :param expired_at: 超期时间。
        :type expired_at: str
        """
        
        

        self._name = None
        self._type = None
        self._content_id = None
        self._subscription_id = None
        self._expired_at = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if content_id is not None:
            self.content_id = content_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if expired_at is not None:
            self.expired_at = expired_at

    @property
    def name(self):
        r"""Gets the name of this WorkflowAsset.

        资产名称。

        :return: The name of this WorkflowAsset.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WorkflowAsset.

        资产名称。

        :param name: The name of this WorkflowAsset.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this WorkflowAsset.

        资产类型，枚举如下: - algorithm：算法 - algorithm2：新算法 - model：模型算法

        :return: The type of this WorkflowAsset.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this WorkflowAsset.

        资产类型，枚举如下: - algorithm：算法 - algorithm2：新算法 - model：模型算法

        :param type: The type of this WorkflowAsset.
        :type type: str
        """
        self._type = type

    @property
    def content_id(self):
        r"""Gets the content_id of this WorkflowAsset.

        资产ID，可在AI Gallery中获取。

        :return: The content_id of this WorkflowAsset.
        :rtype: str
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        r"""Sets the content_id of this WorkflowAsset.

        资产ID，可在AI Gallery中获取。

        :param content_id: The content_id of this WorkflowAsset.
        :type content_id: str
        """
        self._content_id = content_id

    @property
    def subscription_id(self):
        r"""Gets the subscription_id of this WorkflowAsset.

        订阅ID，可在AI Gallery中获取。

        :return: The subscription_id of this WorkflowAsset.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        r"""Sets the subscription_id of this WorkflowAsset.

        订阅ID，可在AI Gallery中获取。

        :param subscription_id: The subscription_id of this WorkflowAsset.
        :type subscription_id: str
        """
        self._subscription_id = subscription_id

    @property
    def expired_at(self):
        r"""Gets the expired_at of this WorkflowAsset.

        超期时间。

        :return: The expired_at of this WorkflowAsset.
        :rtype: str
        """
        return self._expired_at

    @expired_at.setter
    def expired_at(self, expired_at):
        r"""Sets the expired_at of this WorkflowAsset.

        超期时间。

        :param expired_at: The expired_at of this WorkflowAsset.
        :type expired_at: str
        """
        self._expired_at = expired_at

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
        if not isinstance(other, WorkflowAsset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

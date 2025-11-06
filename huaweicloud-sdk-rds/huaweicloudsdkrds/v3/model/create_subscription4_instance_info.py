# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubscription4InstanceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publication_id': 'str',
        'publication_name': 'str'
    }

    attribute_map = {
        'publication_id': 'publication_id',
        'publication_name': 'publication_name'
    }

    def __init__(self, publication_id=None, publication_name=None):
        r"""CreateSubscription4InstanceInfo

        The model defined in huaweicloud sdk

        :param publication_id: 直接创建订阅时，服务器来源为云上实例的发布id。
        :type publication_id: str
        :param publication_name: 直接创建订阅时，服务器来源为云上实例的发布名称。
        :type publication_name: str
        """
        
        

        self._publication_id = None
        self._publication_name = None
        self.discriminator = None

        self.publication_id = publication_id
        if publication_name is not None:
            self.publication_name = publication_name

    @property
    def publication_id(self):
        r"""Gets the publication_id of this CreateSubscription4InstanceInfo.

        直接创建订阅时，服务器来源为云上实例的发布id。

        :return: The publication_id of this CreateSubscription4InstanceInfo.
        :rtype: str
        """
        return self._publication_id

    @publication_id.setter
    def publication_id(self, publication_id):
        r"""Sets the publication_id of this CreateSubscription4InstanceInfo.

        直接创建订阅时，服务器来源为云上实例的发布id。

        :param publication_id: The publication_id of this CreateSubscription4InstanceInfo.
        :type publication_id: str
        """
        self._publication_id = publication_id

    @property
    def publication_name(self):
        r"""Gets the publication_name of this CreateSubscription4InstanceInfo.

        直接创建订阅时，服务器来源为云上实例的发布名称。

        :return: The publication_name of this CreateSubscription4InstanceInfo.
        :rtype: str
        """
        return self._publication_name

    @publication_name.setter
    def publication_name(self, publication_name):
        r"""Sets the publication_name of this CreateSubscription4InstanceInfo.

        直接创建订阅时，服务器来源为云上实例的发布名称。

        :param publication_name: The publication_name of this CreateSubscription4InstanceInfo.
        :type publication_name: str
        """
        self._publication_name = publication_name

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
        if not isinstance(other, CreateSubscription4InstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

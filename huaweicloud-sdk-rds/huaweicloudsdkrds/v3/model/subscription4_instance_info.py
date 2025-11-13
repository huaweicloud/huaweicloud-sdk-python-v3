# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Subscription4InstanceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publication_instance_id': 'str',
        'publication_instance_name': 'str'
    }

    attribute_map = {
        'publication_instance_id': 'publication_instance_id',
        'publication_instance_name': 'publication_instance_name'
    }

    def __init__(self, publication_instance_id=None, publication_instance_name=None):
        r"""Subscription4InstanceInfo

        The model defined in huaweicloud sdk

        :param publication_instance_id: 发布服务器来源为云上实例时的发布实例id。
        :type publication_instance_id: str
        :param publication_instance_name: 发布服务器名称。
        :type publication_instance_name: str
        """
        
        

        self._publication_instance_id = None
        self._publication_instance_name = None
        self.discriminator = None

        if publication_instance_id is not None:
            self.publication_instance_id = publication_instance_id
        if publication_instance_name is not None:
            self.publication_instance_name = publication_instance_name

    @property
    def publication_instance_id(self):
        r"""Gets the publication_instance_id of this Subscription4InstanceInfo.

        发布服务器来源为云上实例时的发布实例id。

        :return: The publication_instance_id of this Subscription4InstanceInfo.
        :rtype: str
        """
        return self._publication_instance_id

    @publication_instance_id.setter
    def publication_instance_id(self, publication_instance_id):
        r"""Sets the publication_instance_id of this Subscription4InstanceInfo.

        发布服务器来源为云上实例时的发布实例id。

        :param publication_instance_id: The publication_instance_id of this Subscription4InstanceInfo.
        :type publication_instance_id: str
        """
        self._publication_instance_id = publication_instance_id

    @property
    def publication_instance_name(self):
        r"""Gets the publication_instance_name of this Subscription4InstanceInfo.

        发布服务器名称。

        :return: The publication_instance_name of this Subscription4InstanceInfo.
        :rtype: str
        """
        return self._publication_instance_name

    @publication_instance_name.setter
    def publication_instance_name(self, publication_instance_name):
        r"""Sets the publication_instance_name of this Subscription4InstanceInfo.

        发布服务器名称。

        :param publication_instance_name: The publication_instance_name of this Subscription4InstanceInfo.
        :type publication_instance_name: str
        """
        self._publication_instance_name = publication_instance_name

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
        if not isinstance(other, Subscription4InstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

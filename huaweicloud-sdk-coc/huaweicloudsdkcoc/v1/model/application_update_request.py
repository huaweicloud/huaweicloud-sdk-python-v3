# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicationUpdateRequest:

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
        'description': 'str',
        'is_collection': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'is_collection': 'is_collection'
    }

    def __init__(self, name=None, description=None, is_collection=None):
        r"""ApplicationUpdateRequest

        The model defined in huaweicloud sdk

        :param name: 修改的应用名称。
        :type name: str
        :param description: 描述。
        :type description: str
        :param is_collection: 是否收藏。
        :type is_collection: bool
        """
        
        

        self._name = None
        self._description = None
        self._is_collection = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if is_collection is not None:
            self.is_collection = is_collection

    @property
    def name(self):
        r"""Gets the name of this ApplicationUpdateRequest.

        修改的应用名称。

        :return: The name of this ApplicationUpdateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ApplicationUpdateRequest.

        修改的应用名称。

        :param name: The name of this ApplicationUpdateRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ApplicationUpdateRequest.

        描述。

        :return: The description of this ApplicationUpdateRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ApplicationUpdateRequest.

        描述。

        :param description: The description of this ApplicationUpdateRequest.
        :type description: str
        """
        self._description = description

    @property
    def is_collection(self):
        r"""Gets the is_collection of this ApplicationUpdateRequest.

        是否收藏。

        :return: The is_collection of this ApplicationUpdateRequest.
        :rtype: bool
        """
        return self._is_collection

    @is_collection.setter
    def is_collection(self, is_collection):
        r"""Sets the is_collection of this ApplicationUpdateRequest.

        是否收藏。

        :param is_collection: The is_collection of this ApplicationUpdateRequest.
        :type is_collection: bool
        """
        self._is_collection = is_collection

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
        if not isinstance(other, ApplicationUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckitemCatalogModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uuid': 'str',
        'name': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'name': 'name'
    }

    def __init__(self, uuid=None, name=None):
        r"""CheckitemCatalogModel

        The model defined in huaweicloud sdk

        :param uuid: 检查项uuid
        :type uuid: str
        :param name: 检查项的名称
        :type name: str
        """
        
        

        self._uuid = None
        self._name = None
        self.discriminator = None

        self.uuid = uuid
        self.name = name

    @property
    def uuid(self):
        r"""Gets the uuid of this CheckitemCatalogModel.

        检查项uuid

        :return: The uuid of this CheckitemCatalogModel.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this CheckitemCatalogModel.

        检查项uuid

        :param uuid: The uuid of this CheckitemCatalogModel.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def name(self):
        r"""Gets the name of this CheckitemCatalogModel.

        检查项的名称

        :return: The name of this CheckitemCatalogModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CheckitemCatalogModel.

        检查项的名称

        :param name: The name of this CheckitemCatalogModel.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, CheckitemCatalogModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

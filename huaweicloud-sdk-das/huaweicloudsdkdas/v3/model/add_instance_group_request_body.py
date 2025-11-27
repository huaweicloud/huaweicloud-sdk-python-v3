# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddInstanceGroupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore_type': 'str',
        'group_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'datastore_type': 'datastore_type',
        'group_name': 'group_name',
        'description': 'description'
    }

    def __init__(self, datastore_type=None, group_name=None, description=None):
        r"""AddInstanceGroupRequestBody

        The model defined in huaweicloud sdk

        :param datastore_type: 数据库类型
        :type datastore_type: str
        :param group_name: 实例组名称
        :type group_name: str
        :param description: 描述
        :type description: str
        """
        
        

        self._datastore_type = None
        self._group_name = None
        self._description = None
        self.discriminator = None

        self.datastore_type = datastore_type
        self.group_name = group_name
        if description is not None:
            self.description = description

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this AddInstanceGroupRequestBody.

        数据库类型

        :return: The datastore_type of this AddInstanceGroupRequestBody.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this AddInstanceGroupRequestBody.

        数据库类型

        :param datastore_type: The datastore_type of this AddInstanceGroupRequestBody.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def group_name(self):
        r"""Gets the group_name of this AddInstanceGroupRequestBody.

        实例组名称

        :return: The group_name of this AddInstanceGroupRequestBody.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this AddInstanceGroupRequestBody.

        实例组名称

        :param group_name: The group_name of this AddInstanceGroupRequestBody.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def description(self):
        r"""Gets the description of this AddInstanceGroupRequestBody.

        描述

        :return: The description of this AddInstanceGroupRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AddInstanceGroupRequestBody.

        描述

        :param description: The description of this AddInstanceGroupRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, AddInstanceGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

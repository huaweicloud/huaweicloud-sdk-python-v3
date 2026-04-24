# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowChildNumRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'region': 'str',
        'x_language': 'str',
        'db_type': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'region': 'region',
        'x_language': 'X-Language',
        'db_type': 'db_type'
    }

    def __init__(self, instance_id=None, region=None, x_language=None, db_type=None):
        r"""ShowChildNumRequest

        The model defined in huaweicloud sdk

        :param instance_id: ddm或者gaussdbv5数据库的实例id
        :type instance_id: str
        :param region: 局点，默认是当前region
        :type region: str
        :param x_language: 请求语言类型。
        :type x_language: str
        :param db_type: 数据库实例的类型
        :type db_type: str
        """
        
        

        self._instance_id = None
        self._region = None
        self._x_language = None
        self._db_type = None
        self.discriminator = None

        self.instance_id = instance_id
        if region is not None:
            self.region = region
        if x_language is not None:
            self.x_language = x_language
        self.db_type = db_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowChildNumRequest.

        ddm或者gaussdbv5数据库的实例id

        :return: The instance_id of this ShowChildNumRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowChildNumRequest.

        ddm或者gaussdbv5数据库的实例id

        :param instance_id: The instance_id of this ShowChildNumRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def region(self):
        r"""Gets the region of this ShowChildNumRequest.

        局点，默认是当前region

        :return: The region of this ShowChildNumRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowChildNumRequest.

        局点，默认是当前region

        :param region: The region of this ShowChildNumRequest.
        :type region: str
        """
        self._region = region

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowChildNumRequest.

        请求语言类型。

        :return: The x_language of this ShowChildNumRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowChildNumRequest.

        请求语言类型。

        :param x_language: The x_language of this ShowChildNumRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def db_type(self):
        r"""Gets the db_type of this ShowChildNumRequest.

        数据库实例的类型

        :return: The db_type of this ShowChildNumRequest.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        r"""Sets the db_type of this ShowChildNumRequest.

        数据库实例的类型

        :param db_type: The db_type of this ShowChildNumRequest.
        :type db_type: str
        """
        self._db_type = db_type

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
        if not isinstance(other, ShowChildNumRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

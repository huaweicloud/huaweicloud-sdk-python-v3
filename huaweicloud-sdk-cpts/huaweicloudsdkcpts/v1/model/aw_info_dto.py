# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AwInfoDTO:

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
        'id': 'str',
        'datum_type': 'int'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'datum_type': 'datumType'
    }

    def __init__(self, name=None, id=None, datum_type=None):
        """AwInfoDTO

        The model defined in huaweicloud sdk

        :param name: aw名
        :type name: str
        :param id: 数据库中dc_case_aw表中的主键ID
        :type id: str
        :param datum_type: 数据类型（用例/aw/事务）
        :type datum_type: int
        """
        
        

        self._name = None
        self._id = None
        self._datum_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if datum_type is not None:
            self.datum_type = datum_type

    @property
    def name(self):
        """Gets the name of this AwInfoDTO.

        aw名

        :return: The name of this AwInfoDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AwInfoDTO.

        aw名

        :param name: The name of this AwInfoDTO.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this AwInfoDTO.

        数据库中dc_case_aw表中的主键ID

        :return: The id of this AwInfoDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AwInfoDTO.

        数据库中dc_case_aw表中的主键ID

        :param id: The id of this AwInfoDTO.
        :type id: str
        """
        self._id = id

    @property
    def datum_type(self):
        """Gets the datum_type of this AwInfoDTO.

        数据类型（用例/aw/事务）

        :return: The datum_type of this AwInfoDTO.
        :rtype: int
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type):
        """Sets the datum_type of this AwInfoDTO.

        数据类型（用例/aw/事务）

        :param datum_type: The datum_type of this AwInfoDTO.
        :type datum_type: int
        """
        self._datum_type = datum_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AwInfoDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

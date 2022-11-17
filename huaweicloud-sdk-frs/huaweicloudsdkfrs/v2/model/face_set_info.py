# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FaceSetInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'face_number': 'int',
        'external_fields': 'object',
        'face_set_id': 'str',
        'face_set_name': 'str',
        'create_date': 'str',
        'face_set_capacity': 'int'
    }

    attribute_map = {
        'face_number': 'face_number',
        'external_fields': 'external_fields',
        'face_set_id': 'face_set_id',
        'face_set_name': 'face_set_name',
        'create_date': 'create_date',
        'face_set_capacity': 'face_set_capacity'
    }

    def __init__(self, face_number=None, external_fields=None, face_set_id=None, face_set_name=None, create_date=None, face_set_capacity=None):
        """FaceSetInfo

        The model defined in huaweicloud sdk

        :param face_number: 人脸库当中的人脸数量。
        :type face_number: int
        :param external_fields: 用户的自定义字段。
        :type external_fields: object
        :param face_set_id: 人脸库ID，随机生成的包含八个字符的字符串。
        :type face_set_id: str
        :param face_set_name: 人脸库名称。
        :type face_set_name: str
        :param create_date: 创建时间。
        :type create_date: str
        :param face_set_capacity: 人脸库最大的容量。
        :type face_set_capacity: int
        """
        
        

        self._face_number = None
        self._external_fields = None
        self._face_set_id = None
        self._face_set_name = None
        self._create_date = None
        self._face_set_capacity = None
        self.discriminator = None

        self.face_number = face_number
        self.external_fields = external_fields
        self.face_set_id = face_set_id
        self.face_set_name = face_set_name
        self.create_date = create_date
        self.face_set_capacity = face_set_capacity

    @property
    def face_number(self):
        """Gets the face_number of this FaceSetInfo.

        人脸库当中的人脸数量。

        :return: The face_number of this FaceSetInfo.
        :rtype: int
        """
        return self._face_number

    @face_number.setter
    def face_number(self, face_number):
        """Sets the face_number of this FaceSetInfo.

        人脸库当中的人脸数量。

        :param face_number: The face_number of this FaceSetInfo.
        :type face_number: int
        """
        self._face_number = face_number

    @property
    def external_fields(self):
        """Gets the external_fields of this FaceSetInfo.

        用户的自定义字段。

        :return: The external_fields of this FaceSetInfo.
        :rtype: object
        """
        return self._external_fields

    @external_fields.setter
    def external_fields(self, external_fields):
        """Sets the external_fields of this FaceSetInfo.

        用户的自定义字段。

        :param external_fields: The external_fields of this FaceSetInfo.
        :type external_fields: object
        """
        self._external_fields = external_fields

    @property
    def face_set_id(self):
        """Gets the face_set_id of this FaceSetInfo.

        人脸库ID，随机生成的包含八个字符的字符串。

        :return: The face_set_id of this FaceSetInfo.
        :rtype: str
        """
        return self._face_set_id

    @face_set_id.setter
    def face_set_id(self, face_set_id):
        """Sets the face_set_id of this FaceSetInfo.

        人脸库ID，随机生成的包含八个字符的字符串。

        :param face_set_id: The face_set_id of this FaceSetInfo.
        :type face_set_id: str
        """
        self._face_set_id = face_set_id

    @property
    def face_set_name(self):
        """Gets the face_set_name of this FaceSetInfo.

        人脸库名称。

        :return: The face_set_name of this FaceSetInfo.
        :rtype: str
        """
        return self._face_set_name

    @face_set_name.setter
    def face_set_name(self, face_set_name):
        """Sets the face_set_name of this FaceSetInfo.

        人脸库名称。

        :param face_set_name: The face_set_name of this FaceSetInfo.
        :type face_set_name: str
        """
        self._face_set_name = face_set_name

    @property
    def create_date(self):
        """Gets the create_date of this FaceSetInfo.

        创建时间。

        :return: The create_date of this FaceSetInfo.
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this FaceSetInfo.

        创建时间。

        :param create_date: The create_date of this FaceSetInfo.
        :type create_date: str
        """
        self._create_date = create_date

    @property
    def face_set_capacity(self):
        """Gets the face_set_capacity of this FaceSetInfo.

        人脸库最大的容量。

        :return: The face_set_capacity of this FaceSetInfo.
        :rtype: int
        """
        return self._face_set_capacity

    @face_set_capacity.setter
    def face_set_capacity(self, face_set_capacity):
        """Sets the face_set_capacity of this FaceSetInfo.

        人脸库最大的容量。

        :param face_set_capacity: The face_set_capacity of this FaceSetInfo.
        :type face_set_capacity: int
        """
        self._face_set_capacity = face_set_capacity

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
        if not isinstance(other, FaceSetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

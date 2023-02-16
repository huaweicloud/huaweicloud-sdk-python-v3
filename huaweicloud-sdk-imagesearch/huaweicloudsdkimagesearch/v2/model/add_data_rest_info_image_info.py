# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDataRestInfoImageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'face_num': 'float',
        'objects': 'list[AddDataRestInfoImageInfoObjects]'
    }

    attribute_map = {
        'face_num': 'face_num',
        'objects': 'objects'
    }

    def __init__(self, face_num=None, objects=None):
        """AddDataRestInfoImageInfo

        The model defined in huaweicloud sdk

        :param face_num: 添加的人脸数量。
        :type face_num: float
        :param objects: 添加的主体列表。
        :type objects: list[:class:`huaweicloudsdkimagesearch.v2.AddDataRestInfoImageInfoObjects`]
        """
        
        

        self._face_num = None
        self._objects = None
        self.discriminator = None

        if face_num is not None:
            self.face_num = face_num
        if objects is not None:
            self.objects = objects

    @property
    def face_num(self):
        """Gets the face_num of this AddDataRestInfoImageInfo.

        添加的人脸数量。

        :return: The face_num of this AddDataRestInfoImageInfo.
        :rtype: float
        """
        return self._face_num

    @face_num.setter
    def face_num(self, face_num):
        """Sets the face_num of this AddDataRestInfoImageInfo.

        添加的人脸数量。

        :param face_num: The face_num of this AddDataRestInfoImageInfo.
        :type face_num: float
        """
        self._face_num = face_num

    @property
    def objects(self):
        """Gets the objects of this AddDataRestInfoImageInfo.

        添加的主体列表。

        :return: The objects of this AddDataRestInfoImageInfo.
        :rtype: list[:class:`huaweicloudsdkimagesearch.v2.AddDataRestInfoImageInfoObjects`]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """Sets the objects of this AddDataRestInfoImageInfo.

        添加的主体列表。

        :param objects: The objects of this AddDataRestInfoImageInfo.
        :type objects: list[:class:`huaweicloudsdkimagesearch.v2.AddDataRestInfoImageInfoObjects`]
        """
        self._objects = objects

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
        if not isinstance(other, AddDataRestInfoImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

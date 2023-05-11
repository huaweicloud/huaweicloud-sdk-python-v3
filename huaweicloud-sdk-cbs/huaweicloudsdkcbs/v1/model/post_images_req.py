# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostImagesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'int',
        'name': 'str',
        'file': 'file',
        'resolution_type': 'int'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'file': 'file',
        'resolution_type': 'resolution_type'
    }

    def __init__(self, type=None, name=None, file=None, resolution_type=None):
        """PostImagesReq

        The model defined in huaweicloud sdk

        :param type: 图片类型： 0：背景 最大 1920*1080 2：图标  最大1920*1080 图片格式：jpg，png
        :type type: int
        :param name: 
        :type name: str
        :param file: 图片文件
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param resolution_type: 横竖屏模式 0：横屏（默认） 1：竖屏
        :type resolution_type: int
        """
        
        

        self._type = None
        self._name = None
        self._file = None
        self._resolution_type = None
        self.discriminator = None

        self.type = type
        self.name = name
        self.file = file
        if resolution_type is not None:
            self.resolution_type = resolution_type

    @property
    def type(self):
        """Gets the type of this PostImagesReq.

        图片类型： 0：背景 最大 1920*1080 2：图标  最大1920*1080 图片格式：jpg，png

        :return: The type of this PostImagesReq.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PostImagesReq.

        图片类型： 0：背景 最大 1920*1080 2：图标  最大1920*1080 图片格式：jpg，png

        :param type: The type of this PostImagesReq.
        :type type: int
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this PostImagesReq.

        :return: The name of this PostImagesReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostImagesReq.

        :param name: The name of this PostImagesReq.
        :type name: str
        """
        self._name = name

    @property
    def file(self):
        """Gets the file of this PostImagesReq.

        图片文件

        :return: The file of this PostImagesReq.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this PostImagesReq.

        图片文件

        :param file: The file of this PostImagesReq.
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._file = file

    @property
    def resolution_type(self):
        """Gets the resolution_type of this PostImagesReq.

        横竖屏模式 0：横屏（默认） 1：竖屏

        :return: The resolution_type of this PostImagesReq.
        :rtype: int
        """
        return self._resolution_type

    @resolution_type.setter
    def resolution_type(self, resolution_type):
        """Sets the resolution_type of this PostImagesReq.

        横竖屏模式 0：横屏（默认） 1：竖屏

        :param resolution_type: The resolution_type of this PostImagesReq.
        :type resolution_type: int
        """
        self._resolution_type = resolution_type

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
        if not isinstance(other, PostImagesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNotebookReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'storages': 'list[NotebookStorage]',
        'flavor': 'FlavorInfo',
        'image': 'NotebookImage',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'storages': 'storages',
        'flavor': 'flavor',
        'image': 'image',
        'name': 'name'
    }

    def __init__(self, description=None, storages=None, flavor=None, image=None, name=None):
        """CreateNotebookReq

        The model defined in huaweicloud sdk

        :param description: 描述信息，取值范围[0,1024]
        :type description: str
        :param storages: 挂载信息
        :type storages: list[:class:`huaweicloudsdkeihealth.v1.NotebookStorage`]
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkeihealth.v1.FlavorInfo`
        :param image: 
        :type image: :class:`huaweicloudsdkeihealth.v1.NotebookImage`
        :param name: notebook名称，取值范围[1,63],仅支持小写字母、数字、中划线(-),开始只能是小写字母，结束只能是小写字母或数字
        :type name: str
        """
        
        

        self._description = None
        self._storages = None
        self._flavor = None
        self._image = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.storages = storages
        self.flavor = flavor
        self.image = image
        self.name = name

    @property
    def description(self):
        """Gets the description of this CreateNotebookReq.

        描述信息，取值范围[0,1024]

        :return: The description of this CreateNotebookReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateNotebookReq.

        描述信息，取值范围[0,1024]

        :param description: The description of this CreateNotebookReq.
        :type description: str
        """
        self._description = description

    @property
    def storages(self):
        """Gets the storages of this CreateNotebookReq.

        挂载信息

        :return: The storages of this CreateNotebookReq.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.NotebookStorage`]
        """
        return self._storages

    @storages.setter
    def storages(self, storages):
        """Sets the storages of this CreateNotebookReq.

        挂载信息

        :param storages: The storages of this CreateNotebookReq.
        :type storages: list[:class:`huaweicloudsdkeihealth.v1.NotebookStorage`]
        """
        self._storages = storages

    @property
    def flavor(self):
        """Gets the flavor of this CreateNotebookReq.

        :return: The flavor of this CreateNotebookReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.FlavorInfo`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this CreateNotebookReq.

        :param flavor: The flavor of this CreateNotebookReq.
        :type flavor: :class:`huaweicloudsdkeihealth.v1.FlavorInfo`
        """
        self._flavor = flavor

    @property
    def image(self):
        """Gets the image of this CreateNotebookReq.

        :return: The image of this CreateNotebookReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.NotebookImage`
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this CreateNotebookReq.

        :param image: The image of this CreateNotebookReq.
        :type image: :class:`huaweicloudsdkeihealth.v1.NotebookImage`
        """
        self._image = image

    @property
    def name(self):
        """Gets the name of this CreateNotebookReq.

        notebook名称，取值范围[1,63],仅支持小写字母、数字、中划线(-),开始只能是小写字母，结束只能是小写字母或数字

        :return: The name of this CreateNotebookReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateNotebookReq.

        notebook名称，取值范围[1,63],仅支持小写字母、数字、中划线(-),开始只能是小写字母，结束只能是小写字母或数字

        :param name: The name of this CreateNotebookReq.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, CreateNotebookReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

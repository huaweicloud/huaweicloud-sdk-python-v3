# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAimTemplateMaterialsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'file_name': 'str',
        'material_id': 'str',
        'aim_resource_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'file_name': 'file_name',
        'material_id': 'material_id',
        'aim_resource_id': 'aim_resource_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, resource_type=None, file_name=None, material_id=None, aim_resource_id=None, offset=None, limit=None):
        r"""ListAimTemplateMaterialsRequest

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型。 - image：表示图片 - video：表示视频 
        :type resource_type: str
        :param file_name: 文件名称。
        :type file_name: str
        :param material_id: 素材ID。
        :type material_id: str
        :param aim_resource_id: 资源ID。
        :type aim_resource_id: str
        :param offset: 翻页页数，从1开始。
        :type offset: int
        :param limit: 每页展示的条数。
        :type limit: int
        """
        
        

        self._resource_type = None
        self._file_name = None
        self._material_id = None
        self._aim_resource_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.resource_type = resource_type
        if file_name is not None:
            self.file_name = file_name
        if material_id is not None:
            self.material_id = material_id
        if aim_resource_id is not None:
            self.aim_resource_id = aim_resource_id
        self.offset = offset
        self.limit = limit

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListAimTemplateMaterialsRequest.

        资源类型。 - image：表示图片 - video：表示视频 

        :return: The resource_type of this ListAimTemplateMaterialsRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListAimTemplateMaterialsRequest.

        资源类型。 - image：表示图片 - video：表示视频 

        :param resource_type: The resource_type of this ListAimTemplateMaterialsRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def file_name(self):
        r"""Gets the file_name of this ListAimTemplateMaterialsRequest.

        文件名称。

        :return: The file_name of this ListAimTemplateMaterialsRequest.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ListAimTemplateMaterialsRequest.

        文件名称。

        :param file_name: The file_name of this ListAimTemplateMaterialsRequest.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def material_id(self):
        r"""Gets the material_id of this ListAimTemplateMaterialsRequest.

        素材ID。

        :return: The material_id of this ListAimTemplateMaterialsRequest.
        :rtype: str
        """
        return self._material_id

    @material_id.setter
    def material_id(self, material_id):
        r"""Sets the material_id of this ListAimTemplateMaterialsRequest.

        素材ID。

        :param material_id: The material_id of this ListAimTemplateMaterialsRequest.
        :type material_id: str
        """
        self._material_id = material_id

    @property
    def aim_resource_id(self):
        r"""Gets the aim_resource_id of this ListAimTemplateMaterialsRequest.

        资源ID。

        :return: The aim_resource_id of this ListAimTemplateMaterialsRequest.
        :rtype: str
        """
        return self._aim_resource_id

    @aim_resource_id.setter
    def aim_resource_id(self, aim_resource_id):
        r"""Sets the aim_resource_id of this ListAimTemplateMaterialsRequest.

        资源ID。

        :param aim_resource_id: The aim_resource_id of this ListAimTemplateMaterialsRequest.
        :type aim_resource_id: str
        """
        self._aim_resource_id = aim_resource_id

    @property
    def offset(self):
        r"""Gets the offset of this ListAimTemplateMaterialsRequest.

        翻页页数，从1开始。

        :return: The offset of this ListAimTemplateMaterialsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAimTemplateMaterialsRequest.

        翻页页数，从1开始。

        :param offset: The offset of this ListAimTemplateMaterialsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAimTemplateMaterialsRequest.

        每页展示的条数。

        :return: The limit of this ListAimTemplateMaterialsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAimTemplateMaterialsRequest.

        每页展示的条数。

        :param limit: The limit of this ListAimTemplateMaterialsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListAimTemplateMaterialsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

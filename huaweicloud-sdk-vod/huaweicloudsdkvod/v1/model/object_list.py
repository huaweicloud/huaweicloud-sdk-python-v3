# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object': 'str',
        'asset_id': 'str',
        'meta_data': 'ObjectMetaData'
    }

    attribute_map = {
        'object': 'object',
        'asset_id': 'asset_id',
        'meta_data': 'meta_data'
    }

    def __init__(self, object=None, asset_id=None, meta_data=None):
        r"""ObjectList

        The model defined in huaweicloud sdk

        :param object: 对象文件名 
        :type object: str
        :param asset_id: 媒资ID 
        :type asset_id: str
        :param meta_data: 
        :type meta_data: :class:`huaweicloudsdkvod.v1.ObjectMetaData`
        """
        
        

        self._object = None
        self._asset_id = None
        self._meta_data = None
        self.discriminator = None

        if object is not None:
            self.object = object
        if asset_id is not None:
            self.asset_id = asset_id
        if meta_data is not None:
            self.meta_data = meta_data

    @property
    def object(self):
        r"""Gets the object of this ObjectList.

        对象文件名 

        :return: The object of this ObjectList.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        r"""Sets the object of this ObjectList.

        对象文件名 

        :param object: The object of this ObjectList.
        :type object: str
        """
        self._object = object

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ObjectList.

        媒资ID 

        :return: The asset_id of this ObjectList.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ObjectList.

        媒资ID 

        :param asset_id: The asset_id of this ObjectList.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def meta_data(self):
        r"""Gets the meta_data of this ObjectList.

        :return: The meta_data of this ObjectList.
        :rtype: :class:`huaweicloudsdkvod.v1.ObjectMetaData`
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        r"""Sets the meta_data of this ObjectList.

        :param meta_data: The meta_data of this ObjectList.
        :type meta_data: :class:`huaweicloudsdkvod.v1.ObjectMetaData`
        """
        self._meta_data = meta_data

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
        if not isinstance(other, ObjectList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

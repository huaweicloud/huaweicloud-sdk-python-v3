# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDataTransformationReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_info': 'list[CreateDataCompareDatabaseObject]',
        'transformation_info': 'CreateDataCompareTransformationInfo'
    }

    attribute_map = {
        'object_info': 'object_info',
        'transformation_info': 'transformation_info'
    }

    def __init__(self, object_info=None, transformation_info=None):
        r"""AddDataTransformationReq

        The model defined in huaweicloud sdk

        :param object_info: 对象信息。
        :type object_info: list[:class:`huaweicloudsdkdrs.v3.CreateDataCompareDatabaseObject`]
        :param transformation_info: 
        :type transformation_info: :class:`huaweicloudsdkdrs.v3.CreateDataCompareTransformationInfo`
        """
        
        

        self._object_info = None
        self._transformation_info = None
        self.discriminator = None

        self.object_info = object_info
        self.transformation_info = transformation_info

    @property
    def object_info(self):
        r"""Gets the object_info of this AddDataTransformationReq.

        对象信息。

        :return: The object_info of this AddDataTransformationReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.CreateDataCompareDatabaseObject`]
        """
        return self._object_info

    @object_info.setter
    def object_info(self, object_info):
        r"""Sets the object_info of this AddDataTransformationReq.

        对象信息。

        :param object_info: The object_info of this AddDataTransformationReq.
        :type object_info: list[:class:`huaweicloudsdkdrs.v3.CreateDataCompareDatabaseObject`]
        """
        self._object_info = object_info

    @property
    def transformation_info(self):
        r"""Gets the transformation_info of this AddDataTransformationReq.

        :return: The transformation_info of this AddDataTransformationReq.
        :rtype: :class:`huaweicloudsdkdrs.v3.CreateDataCompareTransformationInfo`
        """
        return self._transformation_info

    @transformation_info.setter
    def transformation_info(self, transformation_info):
        r"""Sets the transformation_info of this AddDataTransformationReq.

        :param transformation_info: The transformation_info of this AddDataTransformationReq.
        :type transformation_info: :class:`huaweicloudsdkdrs.v3.CreateDataCompareTransformationInfo`
        """
        self._transformation_info = transformation_info

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
        if not isinstance(other, AddDataTransformationReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

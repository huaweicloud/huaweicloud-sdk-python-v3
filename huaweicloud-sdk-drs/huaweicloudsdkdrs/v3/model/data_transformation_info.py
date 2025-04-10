# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataTransformationInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'transformation_info': 'TransformationInfo',
        'config_transformation': 'ConfigTransformationVo',
        'data_transformation_object_infos': 'list[DataTransformationObjectVO]'
    }

    attribute_map = {
        'transformation_info': 'transformation_info',
        'config_transformation': 'config_transformation',
        'data_transformation_object_infos': 'data_transformation_object_infos'
    }

    def __init__(self, transformation_info=None, config_transformation=None, data_transformation_object_infos=None):
        r"""DataTransformationInfo

        The model defined in huaweicloud sdk

        :param transformation_info: 
        :type transformation_info: :class:`huaweicloudsdkdrs.v3.TransformationInfo`
        :param config_transformation: 
        :type config_transformation: :class:`huaweicloudsdkdrs.v3.ConfigTransformationVo`
        :param data_transformation_object_infos: 数据加工对象。
        :type data_transformation_object_infos: list[:class:`huaweicloudsdkdrs.v3.DataTransformationObjectVO`]
        """
        
        

        self._transformation_info = None
        self._config_transformation = None
        self._data_transformation_object_infos = None
        self.discriminator = None

        if transformation_info is not None:
            self.transformation_info = transformation_info
        if config_transformation is not None:
            self.config_transformation = config_transformation
        if data_transformation_object_infos is not None:
            self.data_transformation_object_infos = data_transformation_object_infos

    @property
    def transformation_info(self):
        r"""Gets the transformation_info of this DataTransformationInfo.

        :return: The transformation_info of this DataTransformationInfo.
        :rtype: :class:`huaweicloudsdkdrs.v3.TransformationInfo`
        """
        return self._transformation_info

    @transformation_info.setter
    def transformation_info(self, transformation_info):
        r"""Sets the transformation_info of this DataTransformationInfo.

        :param transformation_info: The transformation_info of this DataTransformationInfo.
        :type transformation_info: :class:`huaweicloudsdkdrs.v3.TransformationInfo`
        """
        self._transformation_info = transformation_info

    @property
    def config_transformation(self):
        r"""Gets the config_transformation of this DataTransformationInfo.

        :return: The config_transformation of this DataTransformationInfo.
        :rtype: :class:`huaweicloudsdkdrs.v3.ConfigTransformationVo`
        """
        return self._config_transformation

    @config_transformation.setter
    def config_transformation(self, config_transformation):
        r"""Sets the config_transformation of this DataTransformationInfo.

        :param config_transformation: The config_transformation of this DataTransformationInfo.
        :type config_transformation: :class:`huaweicloudsdkdrs.v3.ConfigTransformationVo`
        """
        self._config_transformation = config_transformation

    @property
    def data_transformation_object_infos(self):
        r"""Gets the data_transformation_object_infos of this DataTransformationInfo.

        数据加工对象。

        :return: The data_transformation_object_infos of this DataTransformationInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.DataTransformationObjectVO`]
        """
        return self._data_transformation_object_infos

    @data_transformation_object_infos.setter
    def data_transformation_object_infos(self, data_transformation_object_infos):
        r"""Sets the data_transformation_object_infos of this DataTransformationInfo.

        数据加工对象。

        :param data_transformation_object_infos: The data_transformation_object_infos of this DataTransformationInfo.
        :type data_transformation_object_infos: list[:class:`huaweicloudsdkdrs.v3.DataTransformationObjectVO`]
        """
        self._data_transformation_object_infos = data_transformation_object_infos

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
        if not isinstance(other, DataTransformationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

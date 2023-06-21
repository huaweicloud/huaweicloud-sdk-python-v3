# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApigDataSourcesVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_source_vos': 'list[ApigDataSourceVo]'
    }

    attribute_map = {
        'data_source_vos': 'data_source_vos'
    }

    def __init__(self, data_source_vos=None):
        """ApigDataSourcesVo

        The model defined in huaweicloud sdk

        :param data_source_vos: 数据源结构体
        :type data_source_vos: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigDataSourceVo`]
        """
        
        

        self._data_source_vos = None
        self.discriminator = None

        if data_source_vos is not None:
            self.data_source_vos = data_source_vos

    @property
    def data_source_vos(self):
        """Gets the data_source_vos of this ApigDataSourcesVo.

        数据源结构体

        :return: The data_source_vos of this ApigDataSourcesVo.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigDataSourceVo`]
        """
        return self._data_source_vos

    @data_source_vos.setter
    def data_source_vos(self, data_source_vos):
        """Sets the data_source_vos of this ApigDataSourcesVo.

        数据源结构体

        :param data_source_vos: The data_source_vos of this ApigDataSourcesVo.
        :type data_source_vos: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigDataSourceVo`]
        """
        self._data_source_vos = data_source_vos

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
        if not isinstance(other, ApigDataSourcesVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

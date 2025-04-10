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
        'mode': 'int',
        'visible': 'int',
        'data_source_vos': 'list[ApigDataSourceVo]'
    }

    attribute_map = {
        'mode': 'mode',
        'visible': 'visible',
        'data_source_vos': 'data_source_vos'
    }

    def __init__(self, mode=None, visible=None, data_source_vos=None):
        r"""ApigDataSourcesVo

        The model defined in huaweicloud sdk

        :param mode: 企业模式空间下的数据连接还是简单模式空间下的连接,0:简单模式，1：企业模式
        :type mode: int
        :param visible: 连接是否可见,0：不可见，1：可见
        :type visible: int
        :param data_source_vos: 数据源结构体
        :type data_source_vos: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigDataSourceVo`]
        """
        
        

        self._mode = None
        self._visible = None
        self._data_source_vos = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode
        if visible is not None:
            self.visible = visible
        if data_source_vos is not None:
            self.data_source_vos = data_source_vos

    @property
    def mode(self):
        r"""Gets the mode of this ApigDataSourcesVo.

        企业模式空间下的数据连接还是简单模式空间下的连接,0:简单模式，1：企业模式

        :return: The mode of this ApigDataSourcesVo.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ApigDataSourcesVo.

        企业模式空间下的数据连接还是简单模式空间下的连接,0:简单模式，1：企业模式

        :param mode: The mode of this ApigDataSourcesVo.
        :type mode: int
        """
        self._mode = mode

    @property
    def visible(self):
        r"""Gets the visible of this ApigDataSourcesVo.

        连接是否可见,0：不可见，1：可见

        :return: The visible of this ApigDataSourcesVo.
        :rtype: int
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        r"""Sets the visible of this ApigDataSourcesVo.

        连接是否可见,0：不可见，1：可见

        :param visible: The visible of this ApigDataSourcesVo.
        :type visible: int
        """
        self._visible = visible

    @property
    def data_source_vos(self):
        r"""Gets the data_source_vos of this ApigDataSourcesVo.

        数据源结构体

        :return: The data_source_vos of this ApigDataSourcesVo.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigDataSourceVo`]
        """
        return self._data_source_vos

    @data_source_vos.setter
    def data_source_vos(self, data_source_vos):
        r"""Sets the data_source_vos of this ApigDataSourcesVo.

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

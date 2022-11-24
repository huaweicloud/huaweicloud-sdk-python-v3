# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CollectorConfigModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'line_view_config': 'LineViewConfigModel',
        'detail_view_config': 'DetailViewConfigModel'
    }

    attribute_map = {
        'line_view_config': 'line_view_config',
        'detail_view_config': 'detail_view_config'
    }

    def __init__(self, line_view_config=None, detail_view_config=None):
        """CollectorConfigModel

        The model defined in huaweicloud sdk

        :param line_view_config: 
        :type line_view_config: :class:`huaweicloudsdkapm.v1.LineViewConfigModel`
        :param detail_view_config: 
        :type detail_view_config: :class:`huaweicloudsdkapm.v1.DetailViewConfigModel`
        """
        
        

        self._line_view_config = None
        self._detail_view_config = None
        self.discriminator = None

        if line_view_config is not None:
            self.line_view_config = line_view_config
        if detail_view_config is not None:
            self.detail_view_config = detail_view_config

    @property
    def line_view_config(self):
        """Gets the line_view_config of this CollectorConfigModel.

        :return: The line_view_config of this CollectorConfigModel.
        :rtype: :class:`huaweicloudsdkapm.v1.LineViewConfigModel`
        """
        return self._line_view_config

    @line_view_config.setter
    def line_view_config(self, line_view_config):
        """Sets the line_view_config of this CollectorConfigModel.

        :param line_view_config: The line_view_config of this CollectorConfigModel.
        :type line_view_config: :class:`huaweicloudsdkapm.v1.LineViewConfigModel`
        """
        self._line_view_config = line_view_config

    @property
    def detail_view_config(self):
        """Gets the detail_view_config of this CollectorConfigModel.

        :return: The detail_view_config of this CollectorConfigModel.
        :rtype: :class:`huaweicloudsdkapm.v1.DetailViewConfigModel`
        """
        return self._detail_view_config

    @detail_view_config.setter
    def detail_view_config(self, detail_view_config):
        """Sets the detail_view_config of this CollectorConfigModel.

        :param detail_view_config: The detail_view_config of this CollectorConfigModel.
        :type detail_view_config: :class:`huaweicloudsdkapm.v1.DetailViewConfigModel`
        """
        self._detail_view_config = detail_view_config

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
        if not isinstance(other, CollectorConfigModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

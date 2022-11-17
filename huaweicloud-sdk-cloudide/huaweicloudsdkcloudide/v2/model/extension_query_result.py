# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionQueryResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extensions': 'list[ExtensionAllSnake]',
        'result_metadata': 'list[ResultMetadataSnake]'
    }

    attribute_map = {
        'extensions': 'extensions',
        'result_metadata': 'result_metadata'
    }

    def __init__(self, extensions=None, result_metadata=None):
        """ExtensionQueryResult

        The model defined in huaweicloud sdk

        :param extensions: 插件列表集合
        :type extensions: list[:class:`huaweicloudsdkcloudide.v2.ExtensionAllSnake`]
        :param result_metadata: 结果元数据集合
        :type result_metadata: list[:class:`huaweicloudsdkcloudide.v2.ResultMetadataSnake`]
        """
        
        

        self._extensions = None
        self._result_metadata = None
        self.discriminator = None

        if extensions is not None:
            self.extensions = extensions
        if result_metadata is not None:
            self.result_metadata = result_metadata

    @property
    def extensions(self):
        """Gets the extensions of this ExtensionQueryResult.

        插件列表集合

        :return: The extensions of this ExtensionQueryResult.
        :rtype: list[:class:`huaweicloudsdkcloudide.v2.ExtensionAllSnake`]
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this ExtensionQueryResult.

        插件列表集合

        :param extensions: The extensions of this ExtensionQueryResult.
        :type extensions: list[:class:`huaweicloudsdkcloudide.v2.ExtensionAllSnake`]
        """
        self._extensions = extensions

    @property
    def result_metadata(self):
        """Gets the result_metadata of this ExtensionQueryResult.

        结果元数据集合

        :return: The result_metadata of this ExtensionQueryResult.
        :rtype: list[:class:`huaweicloudsdkcloudide.v2.ResultMetadataSnake`]
        """
        return self._result_metadata

    @result_metadata.setter
    def result_metadata(self, result_metadata):
        """Sets the result_metadata of this ExtensionQueryResult.

        结果元数据集合

        :param result_metadata: The result_metadata of this ExtensionQueryResult.
        :type result_metadata: list[:class:`huaweicloudsdkcloudide.v2.ResultMetadataSnake`]
        """
        self._result_metadata = result_metadata

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
        if not isinstance(other, ExtensionQueryResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessPreview:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_preview_id': 'str',
        'analyzer_id': 'str',
        'configurations': 'Configuration',
        'created_at': 'datetime',
        'status': 'AccessPreviewStatus',
        'status_reason': 'PreviewStatusReason'
    }

    attribute_map = {
        'access_preview_id': 'access_preview_id',
        'analyzer_id': 'analyzer_id',
        'configurations': 'configurations',
        'created_at': 'created_at',
        'status': 'status',
        'status_reason': 'status_reason'
    }

    def __init__(self, access_preview_id=None, analyzer_id=None, configurations=None, created_at=None, status=None, status_reason=None):
        """AccessPreview

        The model defined in huaweicloud sdk

        :param access_preview_id: 访问预览的唯一标识符。
        :type access_preview_id: str
        :param analyzer_id: 分析器的唯一标识符。
        :type analyzer_id: str
        :param configurations: 
        :type configurations: :class:`huaweicloudsdkiamaccessanalyzer.v1.Configuration`
        :param created_at: 访问预览创建时间。
        :type created_at: datetime
        :param status: 
        :type status: :class:`huaweicloudsdkiamaccessanalyzer.v1.AccessPreviewStatus`
        :param status_reason: 
        :type status_reason: :class:`huaweicloudsdkiamaccessanalyzer.v1.PreviewStatusReason`
        """
        
        

        self._access_preview_id = None
        self._analyzer_id = None
        self._configurations = None
        self._created_at = None
        self._status = None
        self._status_reason = None
        self.discriminator = None

        self.access_preview_id = access_preview_id
        self.analyzer_id = analyzer_id
        self.configurations = configurations
        self.created_at = created_at
        self.status = status
        if status_reason is not None:
            self.status_reason = status_reason

    @property
    def access_preview_id(self):
        """Gets the access_preview_id of this AccessPreview.

        访问预览的唯一标识符。

        :return: The access_preview_id of this AccessPreview.
        :rtype: str
        """
        return self._access_preview_id

    @access_preview_id.setter
    def access_preview_id(self, access_preview_id):
        """Sets the access_preview_id of this AccessPreview.

        访问预览的唯一标识符。

        :param access_preview_id: The access_preview_id of this AccessPreview.
        :type access_preview_id: str
        """
        self._access_preview_id = access_preview_id

    @property
    def analyzer_id(self):
        """Gets the analyzer_id of this AccessPreview.

        分析器的唯一标识符。

        :return: The analyzer_id of this AccessPreview.
        :rtype: str
        """
        return self._analyzer_id

    @analyzer_id.setter
    def analyzer_id(self, analyzer_id):
        """Sets the analyzer_id of this AccessPreview.

        分析器的唯一标识符。

        :param analyzer_id: The analyzer_id of this AccessPreview.
        :type analyzer_id: str
        """
        self._analyzer_id = analyzer_id

    @property
    def configurations(self):
        """Gets the configurations of this AccessPreview.

        :return: The configurations of this AccessPreview.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.Configuration`
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """Sets the configurations of this AccessPreview.

        :param configurations: The configurations of this AccessPreview.
        :type configurations: :class:`huaweicloudsdkiamaccessanalyzer.v1.Configuration`
        """
        self._configurations = configurations

    @property
    def created_at(self):
        """Gets the created_at of this AccessPreview.

        访问预览创建时间。

        :return: The created_at of this AccessPreview.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AccessPreview.

        访问预览创建时间。

        :param created_at: The created_at of this AccessPreview.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def status(self):
        """Gets the status of this AccessPreview.

        :return: The status of this AccessPreview.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.AccessPreviewStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccessPreview.

        :param status: The status of this AccessPreview.
        :type status: :class:`huaweicloudsdkiamaccessanalyzer.v1.AccessPreviewStatus`
        """
        self._status = status

    @property
    def status_reason(self):
        """Gets the status_reason of this AccessPreview.

        :return: The status_reason of this AccessPreview.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.PreviewStatusReason`
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        """Sets the status_reason of this AccessPreview.

        :param status_reason: The status_reason of this AccessPreview.
        :type status_reason: :class:`huaweicloudsdkiamaccessanalyzer.v1.PreviewStatusReason`
        """
        self._status_reason = status_reason

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
        if not isinstance(other, AccessPreview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

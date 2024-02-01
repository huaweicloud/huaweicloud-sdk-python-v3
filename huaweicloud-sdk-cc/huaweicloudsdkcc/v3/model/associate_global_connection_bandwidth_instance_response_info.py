# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateGlobalConnectionBandwidthInstanceResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_type': 'str',
        'region_id': 'str',
        'project_id': 'str',
        'result': 'str',
        'message': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'region_id': 'region_id',
        'project_id': 'project_id',
        'result': 'result',
        'message': 'message'
    }

    def __init__(self, resource_id=None, resource_type=None, region_id=None, project_id=None, result=None, message=None):
        """AssociateGlobalConnectionBandwidthInstanceResponseInfo

        The model defined in huaweicloud sdk

        :param resource_id: 功能说明：实例ID。 取值范围：1-36个字符，支持数字、字母、_(下划线)、-（中划线）
        :type resource_id: str
        :param resource_type: 功能说明：实例类型。
        :type resource_type: str
        :param region_id: 功能说明：实例所在region，不填默认\&quot;global\&quot;。
        :type region_id: str
        :param project_id: 功能说明：实例所在region对应的projectId。
        :type project_id: str
        :param result: 功能说明：绑定操作成功还是失败。 - success: 成功 - fail: 失败
        :type result: str
        :param message: 功能说明：绑定操作如果失败，具体的错误信息。
        :type message: str
        """
        
        

        self._resource_id = None
        self._resource_type = None
        self._region_id = None
        self._project_id = None
        self._result = None
        self._message = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if region_id is not None:
            self.region_id = region_id
        if project_id is not None:
            self.project_id = project_id
        if result is not None:
            self.result = result
        if message is not None:
            self.message = message

    @property
    def resource_id(self):
        """Gets the resource_id of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.

        功能说明：实例ID。 取值范围：1-36个字符，支持数字、字母、_(下划线)、-（中划线）

        :return: The resource_id of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.

        功能说明：实例ID。 取值范围：1-36个字符，支持数字、字母、_(下划线)、-（中划线）

        :param resource_id: The resource_id of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.

        功能说明：实例类型。

        :return: The resource_type of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.

        功能说明：实例类型。

        :param resource_type: The resource_type of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def region_id(self):
        """Gets the region_id of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.

        功能说明：实例所在region，不填默认\"global\"。

        :return: The region_id of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.

        功能说明：实例所在region，不填默认\"global\"。

        :param region_id: The region_id of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        """Gets the project_id of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.

        功能说明：实例所在region对应的projectId。

        :return: The project_id of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.

        功能说明：实例所在region对应的projectId。

        :param project_id: The project_id of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def result(self):
        """Gets the result of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.

        功能说明：绑定操作成功还是失败。 - success: 成功 - fail: 失败

        :return: The result of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.

        功能说明：绑定操作成功还是失败。 - success: 成功 - fail: 失败

        :param result: The result of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.
        :type result: str
        """
        self._result = result

    @property
    def message(self):
        """Gets the message of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.

        功能说明：绑定操作如果失败，具体的错误信息。

        :return: The message of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.

        功能说明：绑定操作如果失败，具体的错误信息。

        :param message: The message of this AssociateGlobalConnectionBandwidthInstanceResponseInfo.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, AssociateGlobalConnectionBandwidthInstanceResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

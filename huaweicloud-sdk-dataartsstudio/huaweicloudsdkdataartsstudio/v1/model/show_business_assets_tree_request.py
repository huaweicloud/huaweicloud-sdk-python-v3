# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBusinessAssetsTreeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'guid': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'guid': 'guid'
    }

    def __init__(self, workspace=None, guid=None):
        r"""ShowBusinessAssetsTreeRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)
        :type workspace: str
        :param guid: 资产guid，未填充时查询LV1级别业务资产,获取方法请参见[数据开发作业ID](dataartsstudio_02_0351.xml)
        :type guid: str
        """
        
        

        self._workspace = None
        self._guid = None
        self.discriminator = None

        self.workspace = workspace
        if guid is not None:
            self.guid = guid

    @property
    def workspace(self):
        r"""Gets the workspace of this ShowBusinessAssetsTreeRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)

        :return: The workspace of this ShowBusinessAssetsTreeRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ShowBusinessAssetsTreeRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)

        :param workspace: The workspace of this ShowBusinessAssetsTreeRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def guid(self):
        r"""Gets the guid of this ShowBusinessAssetsTreeRequest.

        资产guid，未填充时查询LV1级别业务资产,获取方法请参见[数据开发作业ID](dataartsstudio_02_0351.xml)

        :return: The guid of this ShowBusinessAssetsTreeRequest.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        r"""Sets the guid of this ShowBusinessAssetsTreeRequest.

        资产guid，未填充时查询LV1级别业务资产,获取方法请参见[数据开发作业ID](dataartsstudio_02_0351.xml)

        :param guid: The guid of this ShowBusinessAssetsTreeRequest.
        :type guid: str
        """
        self._guid = guid

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
        if not isinstance(other, ShowBusinessAssetsTreeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

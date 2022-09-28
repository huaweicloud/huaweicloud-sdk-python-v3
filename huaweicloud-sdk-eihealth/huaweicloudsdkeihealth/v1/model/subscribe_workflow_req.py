# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscribeWorkflowReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'asset_version': 'str',
        'destination_workflow_name': 'str',
        'destination_workflow_version': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'asset_version': 'asset_version',
        'destination_workflow_name': 'destination_workflow_name',
        'destination_workflow_version': 'destination_workflow_version'
    }

    def __init__(self, asset_id=None, asset_version=None, destination_workflow_name=None, destination_workflow_version=None):
        """SubscribeWorkflowReq

        The model defined in huaweicloud sdk

        :param asset_id: 资产id。长度1-64，只能包含字母、数字、下划线和中划线
        :type asset_id: str
        :param asset_version: 资产版本。长度1-128，字母或数字开头，后面跟小写字母、数字、小数点、斜杠、下划线或中划线
        :type asset_version: str
        :param destination_workflow_name: 目标流程名称。取值范围[1,56]，允许大小写字母、数字、以及特殊字符中划线(-)和下划线(_)。
        :type destination_workflow_name: str
        :param destination_workflow_version: 目标流程版本。取值范围：长度[1,24]，以小写字母或数字或大写字母开头，允许出现中划线，必须以小写字母或数字或大写字母结尾。
        :type destination_workflow_version: str
        """
        
        

        self._asset_id = None
        self._asset_version = None
        self._destination_workflow_name = None
        self._destination_workflow_version = None
        self.discriminator = None

        self.asset_id = asset_id
        self.asset_version = asset_version
        self.destination_workflow_name = destination_workflow_name
        self.destination_workflow_version = destination_workflow_version

    @property
    def asset_id(self):
        """Gets the asset_id of this SubscribeWorkflowReq.

        资产id。长度1-64，只能包含字母、数字、下划线和中划线

        :return: The asset_id of this SubscribeWorkflowReq.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this SubscribeWorkflowReq.

        资产id。长度1-64，只能包含字母、数字、下划线和中划线

        :param asset_id: The asset_id of this SubscribeWorkflowReq.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def asset_version(self):
        """Gets the asset_version of this SubscribeWorkflowReq.

        资产版本。长度1-128，字母或数字开头，后面跟小写字母、数字、小数点、斜杠、下划线或中划线

        :return: The asset_version of this SubscribeWorkflowReq.
        :rtype: str
        """
        return self._asset_version

    @asset_version.setter
    def asset_version(self, asset_version):
        """Sets the asset_version of this SubscribeWorkflowReq.

        资产版本。长度1-128，字母或数字开头，后面跟小写字母、数字、小数点、斜杠、下划线或中划线

        :param asset_version: The asset_version of this SubscribeWorkflowReq.
        :type asset_version: str
        """
        self._asset_version = asset_version

    @property
    def destination_workflow_name(self):
        """Gets the destination_workflow_name of this SubscribeWorkflowReq.

        目标流程名称。取值范围[1,56]，允许大小写字母、数字、以及特殊字符中划线(-)和下划线(_)。

        :return: The destination_workflow_name of this SubscribeWorkflowReq.
        :rtype: str
        """
        return self._destination_workflow_name

    @destination_workflow_name.setter
    def destination_workflow_name(self, destination_workflow_name):
        """Sets the destination_workflow_name of this SubscribeWorkflowReq.

        目标流程名称。取值范围[1,56]，允许大小写字母、数字、以及特殊字符中划线(-)和下划线(_)。

        :param destination_workflow_name: The destination_workflow_name of this SubscribeWorkflowReq.
        :type destination_workflow_name: str
        """
        self._destination_workflow_name = destination_workflow_name

    @property
    def destination_workflow_version(self):
        """Gets the destination_workflow_version of this SubscribeWorkflowReq.

        目标流程版本。取值范围：长度[1,24]，以小写字母或数字或大写字母开头，允许出现中划线，必须以小写字母或数字或大写字母结尾。

        :return: The destination_workflow_version of this SubscribeWorkflowReq.
        :rtype: str
        """
        return self._destination_workflow_version

    @destination_workflow_version.setter
    def destination_workflow_version(self, destination_workflow_version):
        """Sets the destination_workflow_version of this SubscribeWorkflowReq.

        目标流程版本。取值范围：长度[1,24]，以小写字母或数字或大写字母开头，允许出现中划线，必须以小写字母或数字或大写字母结尾。

        :param destination_workflow_version: The destination_workflow_version of this SubscribeWorkflowReq.
        :type destination_workflow_version: str
        """
        self._destination_workflow_version = destination_workflow_version

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
        if not isinstance(other, SubscribeWorkflowReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

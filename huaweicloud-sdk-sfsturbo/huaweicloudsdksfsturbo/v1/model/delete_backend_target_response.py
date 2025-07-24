# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteBackendTargetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_id': 'str',
        'delete_data_in_file_system': 'bool',
        'lifecycle': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'target_id': 'target_id',
        'delete_data_in_file_system': 'delete_data_in_file_system',
        'lifecycle': 'lifecycle',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, target_id=None, delete_data_in_file_system=None, lifecycle=None, x_request_id=None):
        r"""DeleteBackendTargetResponse

        The model defined in huaweicloud sdk

        :param target_id: 绑定关系ID
        :type target_id: str
        :param delete_data_in_file_system: 删除后端存储时是否同时删除文件系统内的联动目录及其数据文件
        :type delete_data_in_file_system: bool
        :param lifecycle: 绑定状态。只支持DELETING和FAILED
        :type lifecycle: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(DeleteBackendTargetResponse, self).__init__()

        self._target_id = None
        self._delete_data_in_file_system = None
        self._lifecycle = None
        self._x_request_id = None
        self.discriminator = None

        if target_id is not None:
            self.target_id = target_id
        if delete_data_in_file_system is not None:
            self.delete_data_in_file_system = delete_data_in_file_system
        if lifecycle is not None:
            self.lifecycle = lifecycle
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def target_id(self):
        r"""Gets the target_id of this DeleteBackendTargetResponse.

        绑定关系ID

        :return: The target_id of this DeleteBackendTargetResponse.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this DeleteBackendTargetResponse.

        绑定关系ID

        :param target_id: The target_id of this DeleteBackendTargetResponse.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def delete_data_in_file_system(self):
        r"""Gets the delete_data_in_file_system of this DeleteBackendTargetResponse.

        删除后端存储时是否同时删除文件系统内的联动目录及其数据文件

        :return: The delete_data_in_file_system of this DeleteBackendTargetResponse.
        :rtype: bool
        """
        return self._delete_data_in_file_system

    @delete_data_in_file_system.setter
    def delete_data_in_file_system(self, delete_data_in_file_system):
        r"""Sets the delete_data_in_file_system of this DeleteBackendTargetResponse.

        删除后端存储时是否同时删除文件系统内的联动目录及其数据文件

        :param delete_data_in_file_system: The delete_data_in_file_system of this DeleteBackendTargetResponse.
        :type delete_data_in_file_system: bool
        """
        self._delete_data_in_file_system = delete_data_in_file_system

    @property
    def lifecycle(self):
        r"""Gets the lifecycle of this DeleteBackendTargetResponse.

        绑定状态。只支持DELETING和FAILED

        :return: The lifecycle of this DeleteBackendTargetResponse.
        :rtype: str
        """
        return self._lifecycle

    @lifecycle.setter
    def lifecycle(self, lifecycle):
        r"""Sets the lifecycle of this DeleteBackendTargetResponse.

        绑定状态。只支持DELETING和FAILED

        :param lifecycle: The lifecycle of this DeleteBackendTargetResponse.
        :type lifecycle: str
        """
        self._lifecycle = lifecycle

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this DeleteBackendTargetResponse.

        :return: The x_request_id of this DeleteBackendTargetResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this DeleteBackendTargetResponse.

        :param x_request_id: The x_request_id of this DeleteBackendTargetResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, DeleteBackendTargetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebTamperPrivilegedProcessRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'privileged_process_path_list': 'list[str]',
        'privileged_child_status': 'bool'
    }

    attribute_map = {
        'privileged_process_path_list': 'privileged_process_path_list',
        'privileged_child_status': 'privileged_child_status'
    }

    def __init__(self, privileged_process_path_list=None, privileged_child_status=None):
        r"""WebTamperPrivilegedProcessRequestInfo

        The model defined in huaweicloud sdk

        :param privileged_process_path_list: 特权进程路径集合
        :type privileged_process_path_list: list[str]
        :param privileged_child_status: 特权进程子进程可信状态
        :type privileged_child_status: bool
        """
        
        

        self._privileged_process_path_list = None
        self._privileged_child_status = None
        self.discriminator = None

        if privileged_process_path_list is not None:
            self.privileged_process_path_list = privileged_process_path_list
        if privileged_child_status is not None:
            self.privileged_child_status = privileged_child_status

    @property
    def privileged_process_path_list(self):
        r"""Gets the privileged_process_path_list of this WebTamperPrivilegedProcessRequestInfo.

        特权进程路径集合

        :return: The privileged_process_path_list of this WebTamperPrivilegedProcessRequestInfo.
        :rtype: list[str]
        """
        return self._privileged_process_path_list

    @privileged_process_path_list.setter
    def privileged_process_path_list(self, privileged_process_path_list):
        r"""Sets the privileged_process_path_list of this WebTamperPrivilegedProcessRequestInfo.

        特权进程路径集合

        :param privileged_process_path_list: The privileged_process_path_list of this WebTamperPrivilegedProcessRequestInfo.
        :type privileged_process_path_list: list[str]
        """
        self._privileged_process_path_list = privileged_process_path_list

    @property
    def privileged_child_status(self):
        r"""Gets the privileged_child_status of this WebTamperPrivilegedProcessRequestInfo.

        特权进程子进程可信状态

        :return: The privileged_child_status of this WebTamperPrivilegedProcessRequestInfo.
        :rtype: bool
        """
        return self._privileged_child_status

    @privileged_child_status.setter
    def privileged_child_status(self, privileged_child_status):
        r"""Sets the privileged_child_status of this WebTamperPrivilegedProcessRequestInfo.

        特权进程子进程可信状态

        :param privileged_child_status: The privileged_child_status of this WebTamperPrivilegedProcessRequestInfo.
        :type privileged_child_status: bool
        """
        self._privileged_child_status = privileged_child_status

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
        if not isinstance(other, WebTamperPrivilegedProcessRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

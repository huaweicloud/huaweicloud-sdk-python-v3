# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplicationRecordsExtraInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'progress': 'int',
        'fail_code': 'str',
        'fail_reason': 'str',
        'auto_trigger': 'bool',
        'destinatio_vault_id': 'str'
    }

    attribute_map = {
        'progress': 'progress',
        'fail_code': 'fail_code',
        'fail_reason': 'fail_reason',
        'auto_trigger': 'auto_trigger',
        'destinatio_vault_id': 'destinatio_vault_id'
    }

    def __init__(self, progress=None, fail_code=None, fail_reason=None, auto_trigger=None, destinatio_vault_id=None):
        """ReplicationRecordsExtraInfo

        The model defined in huaweicloud sdk

        :param progress: 复制进度
        :type progress: int
        :param fail_code: 失败错误码，成功时为空
        :type fail_code: str
        :param fail_reason: 错误原因
        :type fail_reason: str
        :param auto_trigger: 是否为自动调度复制
        :type auto_trigger: bool
        :param destinatio_vault_id: 目标端的存储库id
        :type destinatio_vault_id: str
        """
        
        

        self._progress = None
        self._fail_code = None
        self._fail_reason = None
        self._auto_trigger = None
        self._destinatio_vault_id = None
        self.discriminator = None

        if progress is not None:
            self.progress = progress
        if fail_code is not None:
            self.fail_code = fail_code
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if auto_trigger is not None:
            self.auto_trigger = auto_trigger
        if destinatio_vault_id is not None:
            self.destinatio_vault_id = destinatio_vault_id

    @property
    def progress(self):
        """Gets the progress of this ReplicationRecordsExtraInfo.

        复制进度

        :return: The progress of this ReplicationRecordsExtraInfo.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ReplicationRecordsExtraInfo.

        复制进度

        :param progress: The progress of this ReplicationRecordsExtraInfo.
        :type progress: int
        """
        self._progress = progress

    @property
    def fail_code(self):
        """Gets the fail_code of this ReplicationRecordsExtraInfo.

        失败错误码，成功时为空

        :return: The fail_code of this ReplicationRecordsExtraInfo.
        :rtype: str
        """
        return self._fail_code

    @fail_code.setter
    def fail_code(self, fail_code):
        """Sets the fail_code of this ReplicationRecordsExtraInfo.

        失败错误码，成功时为空

        :param fail_code: The fail_code of this ReplicationRecordsExtraInfo.
        :type fail_code: str
        """
        self._fail_code = fail_code

    @property
    def fail_reason(self):
        """Gets the fail_reason of this ReplicationRecordsExtraInfo.

        错误原因

        :return: The fail_reason of this ReplicationRecordsExtraInfo.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this ReplicationRecordsExtraInfo.

        错误原因

        :param fail_reason: The fail_reason of this ReplicationRecordsExtraInfo.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def auto_trigger(self):
        """Gets the auto_trigger of this ReplicationRecordsExtraInfo.

        是否为自动调度复制

        :return: The auto_trigger of this ReplicationRecordsExtraInfo.
        :rtype: bool
        """
        return self._auto_trigger

    @auto_trigger.setter
    def auto_trigger(self, auto_trigger):
        """Sets the auto_trigger of this ReplicationRecordsExtraInfo.

        是否为自动调度复制

        :param auto_trigger: The auto_trigger of this ReplicationRecordsExtraInfo.
        :type auto_trigger: bool
        """
        self._auto_trigger = auto_trigger

    @property
    def destinatio_vault_id(self):
        """Gets the destinatio_vault_id of this ReplicationRecordsExtraInfo.

        目标端的存储库id

        :return: The destinatio_vault_id of this ReplicationRecordsExtraInfo.
        :rtype: str
        """
        return self._destinatio_vault_id

    @destinatio_vault_id.setter
    def destinatio_vault_id(self, destinatio_vault_id):
        """Sets the destinatio_vault_id of this ReplicationRecordsExtraInfo.

        目标端的存储库id

        :param destinatio_vault_id: The destinatio_vault_id of this ReplicationRecordsExtraInfo.
        :type destinatio_vault_id: str
        """
        self._destinatio_vault_id = destinatio_vault_id

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
        if not isinstance(other, ReplicationRecordsExtraInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchoverResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'updated_at': 'str',
        'source_db': 'EndpointVO',
        'target_db': 'EndpointVO',
        'job_direction': 'str',
        'is_target_readonly': 'bool',
        'error_msg': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'updated_at': 'updated_at',
        'source_db': 'source_db',
        'target_db': 'target_db',
        'job_direction': 'job_direction',
        'is_target_readonly': 'is_target_readonly',
        'error_msg': 'error_msg',
        'error_code': 'error_code'
    }

    def __init__(self, job_id=None, updated_at=None, source_db=None, target_db=None, job_direction=None, is_target_readonly=None, error_msg=None, error_code=None):
        """SwitchoverResp

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param updated_at: 更新时间，格式yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;
        :type updated_at: str
        :param source_db: 
        :type source_db: :class:`huaweicloudsdkdrs.v3.EndpointVO`
        :param target_db: 
        :type target_db: :class:`huaweicloudsdkdrs.v3.EndpointVO`
        :param job_direction: 任务方向。 - up 入云 灾备场景时对应本云为备 - down 出云 灾备场景时对应本云为主 - non-dbs 自建
        :type job_direction: str
        :param is_target_readonly: 目标库是否只读。
        :type is_target_readonly: bool
        :param error_msg: 错误信息。
        :type error_msg: str
        :param error_code: 错误码。
        :type error_code: str
        """
        
        

        self._job_id = None
        self._updated_at = None
        self._source_db = None
        self._target_db = None
        self._job_direction = None
        self._is_target_readonly = None
        self._error_msg = None
        self._error_code = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if updated_at is not None:
            self.updated_at = updated_at
        if source_db is not None:
            self.source_db = source_db
        if target_db is not None:
            self.target_db = target_db
        if job_direction is not None:
            self.job_direction = job_direction
        if is_target_readonly is not None:
            self.is_target_readonly = is_target_readonly
        if error_msg is not None:
            self.error_msg = error_msg
        if error_code is not None:
            self.error_code = error_code

    @property
    def job_id(self):
        """Gets the job_id of this SwitchoverResp.

        任务ID

        :return: The job_id of this SwitchoverResp.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this SwitchoverResp.

        任务ID

        :param job_id: The job_id of this SwitchoverResp.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def updated_at(self):
        """Gets the updated_at of this SwitchoverResp.

        更新时间，格式yyyy-MM-dd'T'HH:mm:ss'Z'

        :return: The updated_at of this SwitchoverResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SwitchoverResp.

        更新时间，格式yyyy-MM-dd'T'HH:mm:ss'Z'

        :param updated_at: The updated_at of this SwitchoverResp.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def source_db(self):
        """Gets the source_db of this SwitchoverResp.

        :return: The source_db of this SwitchoverResp.
        :rtype: :class:`huaweicloudsdkdrs.v3.EndpointVO`
        """
        return self._source_db

    @source_db.setter
    def source_db(self, source_db):
        """Sets the source_db of this SwitchoverResp.

        :param source_db: The source_db of this SwitchoverResp.
        :type source_db: :class:`huaweicloudsdkdrs.v3.EndpointVO`
        """
        self._source_db = source_db

    @property
    def target_db(self):
        """Gets the target_db of this SwitchoverResp.

        :return: The target_db of this SwitchoverResp.
        :rtype: :class:`huaweicloudsdkdrs.v3.EndpointVO`
        """
        return self._target_db

    @target_db.setter
    def target_db(self, target_db):
        """Sets the target_db of this SwitchoverResp.

        :param target_db: The target_db of this SwitchoverResp.
        :type target_db: :class:`huaweicloudsdkdrs.v3.EndpointVO`
        """
        self._target_db = target_db

    @property
    def job_direction(self):
        """Gets the job_direction of this SwitchoverResp.

        任务方向。 - up 入云 灾备场景时对应本云为备 - down 出云 灾备场景时对应本云为主 - non-dbs 自建

        :return: The job_direction of this SwitchoverResp.
        :rtype: str
        """
        return self._job_direction

    @job_direction.setter
    def job_direction(self, job_direction):
        """Sets the job_direction of this SwitchoverResp.

        任务方向。 - up 入云 灾备场景时对应本云为备 - down 出云 灾备场景时对应本云为主 - non-dbs 自建

        :param job_direction: The job_direction of this SwitchoverResp.
        :type job_direction: str
        """
        self._job_direction = job_direction

    @property
    def is_target_readonly(self):
        """Gets the is_target_readonly of this SwitchoverResp.

        目标库是否只读。

        :return: The is_target_readonly of this SwitchoverResp.
        :rtype: bool
        """
        return self._is_target_readonly

    @is_target_readonly.setter
    def is_target_readonly(self, is_target_readonly):
        """Sets the is_target_readonly of this SwitchoverResp.

        目标库是否只读。

        :param is_target_readonly: The is_target_readonly of this SwitchoverResp.
        :type is_target_readonly: bool
        """
        self._is_target_readonly = is_target_readonly

    @property
    def error_msg(self):
        """Gets the error_msg of this SwitchoverResp.

        错误信息。

        :return: The error_msg of this SwitchoverResp.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this SwitchoverResp.

        错误信息。

        :param error_msg: The error_msg of this SwitchoverResp.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def error_code(self):
        """Gets the error_code of this SwitchoverResp.

        错误码。

        :return: The error_code of this SwitchoverResp.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this SwitchoverResp.

        错误码。

        :param error_code: The error_code of this SwitchoverResp.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, SwitchoverResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

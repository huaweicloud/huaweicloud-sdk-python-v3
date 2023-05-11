# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportFileReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'params': 'object',
        'same_name_policy': 'str',
        'jobs_param': 'object',
        'execute_user': 'str'
    }

    attribute_map = {
        'path': 'path',
        'params': 'params',
        'same_name_policy': 'sameNamePolicy',
        'jobs_param': 'jobsParam',
        'execute_user': 'executeUser'
    }

    def __init__(self, path=None, params=None, same_name_policy=None, jobs_param=None, execute_user=None):
        """ImportFileReq

        The model defined in huaweicloud sdk

        :param path: 
        :type path: str
        :param params: 公共作业参数
        :type params: object
        :param same_name_policy: 
        :type same_name_policy: str
        :param jobs_param: 指定作业参数
        :type jobs_param: object
        :param execute_user: 
        :type execute_user: str
        """
        
        

        self._path = None
        self._params = None
        self._same_name_policy = None
        self._jobs_param = None
        self._execute_user = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if params is not None:
            self.params = params
        if same_name_policy is not None:
            self.same_name_policy = same_name_policy
        if jobs_param is not None:
            self.jobs_param = jobs_param
        if execute_user is not None:
            self.execute_user = execute_user

    @property
    def path(self):
        """Gets the path of this ImportFileReq.

        :return: The path of this ImportFileReq.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ImportFileReq.

        :param path: The path of this ImportFileReq.
        :type path: str
        """
        self._path = path

    @property
    def params(self):
        """Gets the params of this ImportFileReq.

        公共作业参数

        :return: The params of this ImportFileReq.
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ImportFileReq.

        公共作业参数

        :param params: The params of this ImportFileReq.
        :type params: object
        """
        self._params = params

    @property
    def same_name_policy(self):
        """Gets the same_name_policy of this ImportFileReq.

        :return: The same_name_policy of this ImportFileReq.
        :rtype: str
        """
        return self._same_name_policy

    @same_name_policy.setter
    def same_name_policy(self, same_name_policy):
        """Sets the same_name_policy of this ImportFileReq.

        :param same_name_policy: The same_name_policy of this ImportFileReq.
        :type same_name_policy: str
        """
        self._same_name_policy = same_name_policy

    @property
    def jobs_param(self):
        """Gets the jobs_param of this ImportFileReq.

        指定作业参数

        :return: The jobs_param of this ImportFileReq.
        :rtype: object
        """
        return self._jobs_param

    @jobs_param.setter
    def jobs_param(self, jobs_param):
        """Sets the jobs_param of this ImportFileReq.

        指定作业参数

        :param jobs_param: The jobs_param of this ImportFileReq.
        :type jobs_param: object
        """
        self._jobs_param = jobs_param

    @property
    def execute_user(self):
        """Gets the execute_user of this ImportFileReq.

        :return: The execute_user of this ImportFileReq.
        :rtype: str
        """
        return self._execute_user

    @execute_user.setter
    def execute_user(self, execute_user):
        """Sets the execute_user of this ImportFileReq.

        :param execute_user: The execute_user of this ImportFileReq.
        :type execute_user: str
        """
        self._execute_user = execute_user

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
        if not isinstance(other, ImportFileReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

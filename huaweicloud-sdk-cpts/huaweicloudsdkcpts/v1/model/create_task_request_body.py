# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'project_id': 'int',
        'temps': 'list[str]',
        'operate_mode': 'int',
        'bench_concurrent': 'int'
    }

    attribute_map = {
        'name': 'name',
        'project_id': 'project_id',
        'temps': 'temps',
        'operate_mode': 'operate_mode',
        'bench_concurrent': 'bench_concurrent'
    }

    def __init__(self, name=None, project_id=None, temps=None, operate_mode=None, bench_concurrent=None):
        """CreateTaskRequestBody

        The model defined in huaweicloud sdk

        :param name: name
        :type name: str
        :param project_id: project_id
        :type project_id: int
        :param temps: temps
        :type temps: list[str]
        :param operate_mode: operate_mode
        :type operate_mode: int
        :param bench_concurrent: bench_concurrent
        :type bench_concurrent: int
        """
        
        

        self._name = None
        self._project_id = None
        self._temps = None
        self._operate_mode = None
        self._bench_concurrent = None
        self.discriminator = None

        self.name = name
        self.project_id = project_id
        if temps is not None:
            self.temps = temps
        if operate_mode is not None:
            self.operate_mode = operate_mode
        if bench_concurrent is not None:
            self.bench_concurrent = bench_concurrent

    @property
    def name(self):
        """Gets the name of this CreateTaskRequestBody.

        name

        :return: The name of this CreateTaskRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateTaskRequestBody.

        name

        :param name: The name of this CreateTaskRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this CreateTaskRequestBody.

        project_id

        :return: The project_id of this CreateTaskRequestBody.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateTaskRequestBody.

        project_id

        :param project_id: The project_id of this CreateTaskRequestBody.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def temps(self):
        """Gets the temps of this CreateTaskRequestBody.

        temps

        :return: The temps of this CreateTaskRequestBody.
        :rtype: list[str]
        """
        return self._temps

    @temps.setter
    def temps(self, temps):
        """Sets the temps of this CreateTaskRequestBody.

        temps

        :param temps: The temps of this CreateTaskRequestBody.
        :type temps: list[str]
        """
        self._temps = temps

    @property
    def operate_mode(self):
        """Gets the operate_mode of this CreateTaskRequestBody.

        operate_mode

        :return: The operate_mode of this CreateTaskRequestBody.
        :rtype: int
        """
        return self._operate_mode

    @operate_mode.setter
    def operate_mode(self, operate_mode):
        """Sets the operate_mode of this CreateTaskRequestBody.

        operate_mode

        :param operate_mode: The operate_mode of this CreateTaskRequestBody.
        :type operate_mode: int
        """
        self._operate_mode = operate_mode

    @property
    def bench_concurrent(self):
        """Gets the bench_concurrent of this CreateTaskRequestBody.

        bench_concurrent

        :return: The bench_concurrent of this CreateTaskRequestBody.
        :rtype: int
        """
        return self._bench_concurrent

    @bench_concurrent.setter
    def bench_concurrent(self, bench_concurrent):
        """Sets the bench_concurrent of this CreateTaskRequestBody.

        bench_concurrent

        :param bench_concurrent: The bench_concurrent of this CreateTaskRequestBody.
        :type bench_concurrent: int
        """
        self._bench_concurrent = bench_concurrent

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
        if not isinstance(other, CreateTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

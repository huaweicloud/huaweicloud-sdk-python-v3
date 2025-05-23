# coding: utf-8

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
        r"""CreateTaskRequestBody

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param project_id: 工程id
        :type project_id: int
        :param temps: 事务信息
        :type temps: list[str]
        :param operate_mode: 压力阶段模式，0：时长模式；1：次数模式；2：混合模式
        :type operate_mode: int
        :param bench_concurrent: 基准并发
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
        r"""Gets the name of this CreateTaskRequestBody.

        名称

        :return: The name of this CreateTaskRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateTaskRequestBody.

        名称

        :param name: The name of this CreateTaskRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateTaskRequestBody.

        工程id

        :return: The project_id of this CreateTaskRequestBody.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateTaskRequestBody.

        工程id

        :param project_id: The project_id of this CreateTaskRequestBody.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def temps(self):
        r"""Gets the temps of this CreateTaskRequestBody.

        事务信息

        :return: The temps of this CreateTaskRequestBody.
        :rtype: list[str]
        """
        return self._temps

    @temps.setter
    def temps(self, temps):
        r"""Sets the temps of this CreateTaskRequestBody.

        事务信息

        :param temps: The temps of this CreateTaskRequestBody.
        :type temps: list[str]
        """
        self._temps = temps

    @property
    def operate_mode(self):
        r"""Gets the operate_mode of this CreateTaskRequestBody.

        压力阶段模式，0：时长模式；1：次数模式；2：混合模式

        :return: The operate_mode of this CreateTaskRequestBody.
        :rtype: int
        """
        return self._operate_mode

    @operate_mode.setter
    def operate_mode(self, operate_mode):
        r"""Sets the operate_mode of this CreateTaskRequestBody.

        压力阶段模式，0：时长模式；1：次数模式；2：混合模式

        :param operate_mode: The operate_mode of this CreateTaskRequestBody.
        :type operate_mode: int
        """
        self._operate_mode = operate_mode

    @property
    def bench_concurrent(self):
        r"""Gets the bench_concurrent of this CreateTaskRequestBody.

        基准并发

        :return: The bench_concurrent of this CreateTaskRequestBody.
        :rtype: int
        """
        return self._bench_concurrent

    @bench_concurrent.setter
    def bench_concurrent(self, bench_concurrent):
        r"""Sets the bench_concurrent of this CreateTaskRequestBody.

        基准并发

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

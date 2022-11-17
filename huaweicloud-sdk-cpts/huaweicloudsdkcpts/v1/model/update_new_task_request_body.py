# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNewTaskRequestBody:

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
        'parallel': 'bool',
        'project_id': 'int',
        'operate_mode': 'int',
        'case_id_list': 'list[int]'
    }

    attribute_map = {
        'name': 'name',
        'parallel': 'parallel',
        'project_id': 'project_id',
        'operate_mode': 'operate_mode',
        'case_id_list': 'case_id_list'
    }

    def __init__(self, name=None, parallel=None, project_id=None, operate_mode=None, case_id_list=None):
        """UpdateNewTaskRequestBody

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param parallel: 并行状态(表示任务执行时用例是否并行执行;true:并行执行,false:串行执行)
        :type parallel: bool
        :param project_id: 工程id
        :type project_id: int
        :param operate_mode: 任务模式(兼容旧版接口保留字段,0:时长模式,1:次数模式,2:混合模式;此处请传固定值:2)
        :type operate_mode: int
        :param case_id_list: 关联的用例id集合
        :type case_id_list: list[int]
        """
        
        

        self._name = None
        self._parallel = None
        self._project_id = None
        self._operate_mode = None
        self._case_id_list = None
        self.discriminator = None

        self.name = name
        self.parallel = parallel
        self.project_id = project_id
        self.operate_mode = operate_mode
        self.case_id_list = case_id_list

    @property
    def name(self):
        """Gets the name of this UpdateNewTaskRequestBody.

        名称

        :return: The name of this UpdateNewTaskRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateNewTaskRequestBody.

        名称

        :param name: The name of this UpdateNewTaskRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def parallel(self):
        """Gets the parallel of this UpdateNewTaskRequestBody.

        并行状态(表示任务执行时用例是否并行执行;true:并行执行,false:串行执行)

        :return: The parallel of this UpdateNewTaskRequestBody.
        :rtype: bool
        """
        return self._parallel

    @parallel.setter
    def parallel(self, parallel):
        """Sets the parallel of this UpdateNewTaskRequestBody.

        并行状态(表示任务执行时用例是否并行执行;true:并行执行,false:串行执行)

        :param parallel: The parallel of this UpdateNewTaskRequestBody.
        :type parallel: bool
        """
        self._parallel = parallel

    @property
    def project_id(self):
        """Gets the project_id of this UpdateNewTaskRequestBody.

        工程id

        :return: The project_id of this UpdateNewTaskRequestBody.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UpdateNewTaskRequestBody.

        工程id

        :param project_id: The project_id of this UpdateNewTaskRequestBody.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def operate_mode(self):
        """Gets the operate_mode of this UpdateNewTaskRequestBody.

        任务模式(兼容旧版接口保留字段,0:时长模式,1:次数模式,2:混合模式;此处请传固定值:2)

        :return: The operate_mode of this UpdateNewTaskRequestBody.
        :rtype: int
        """
        return self._operate_mode

    @operate_mode.setter
    def operate_mode(self, operate_mode):
        """Sets the operate_mode of this UpdateNewTaskRequestBody.

        任务模式(兼容旧版接口保留字段,0:时长模式,1:次数模式,2:混合模式;此处请传固定值:2)

        :param operate_mode: The operate_mode of this UpdateNewTaskRequestBody.
        :type operate_mode: int
        """
        self._operate_mode = operate_mode

    @property
    def case_id_list(self):
        """Gets the case_id_list of this UpdateNewTaskRequestBody.

        关联的用例id集合

        :return: The case_id_list of this UpdateNewTaskRequestBody.
        :rtype: list[int]
        """
        return self._case_id_list

    @case_id_list.setter
    def case_id_list(self, case_id_list):
        """Sets the case_id_list of this UpdateNewTaskRequestBody.

        关联的用例id集合

        :param case_id_list: The case_id_list of this UpdateNewTaskRequestBody.
        :type case_id_list: list[int]
        """
        self._case_id_list = case_id_list

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
        if not isinstance(other, UpdateNewTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

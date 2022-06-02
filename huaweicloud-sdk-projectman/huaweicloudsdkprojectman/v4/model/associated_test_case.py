# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociatedTestCase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'case_id': 'str',
        'case_num': 'str',
        'case_name': 'str',
        'case_level': 'str',
        'status': 'StatusVo',
        'creator': 'SimpleUser',
        'owner': 'SimpleUser',
        'project': 'SimpleProject',
        'is_base_line': 'int',
        'type': 'str',
        'created_time': 'int'
    }

    attribute_map = {
        'case_id': 'case_id',
        'case_num': 'case_num',
        'case_name': 'case_name',
        'case_level': 'case_level',
        'status': 'status',
        'creator': 'creator',
        'owner': 'owner',
        'project': 'project',
        'is_base_line': 'is_base_line',
        'type': 'type',
        'created_time': 'created_time'
    }

    def __init__(self, case_id=None, case_num=None, case_name=None, case_level=None, status=None, creator=None, owner=None, project=None, is_base_line=None, type=None, created_time=None):
        """AssociatedTestCase

        The model defined in huaweicloud sdk

        :param case_id: 用例ID
        :type case_id: str
        :param case_num: 用例编号
        :type case_num: str
        :param case_name: 用例名称
        :type case_name: str
        :param case_level: 用例等级
        :type case_level: str
        :param status: 
        :type status: :class:`huaweicloudsdkprojectman.v4.StatusVo`
        :param creator: 
        :type creator: :class:`huaweicloudsdkprojectman.v4.SimpleUser`
        :param owner: 
        :type owner: :class:`huaweicloudsdkprojectman.v4.SimpleUser`
        :param project: 
        :type project: :class:`huaweicloudsdkprojectman.v4.SimpleProject`
        :param is_base_line: 是否基线
        :type is_base_line: int
        :param type: 用例类型
        :type type: str
        :param created_time: 创建时间
        :type created_time: int
        """
        
        

        self._case_id = None
        self._case_num = None
        self._case_name = None
        self._case_level = None
        self._status = None
        self._creator = None
        self._owner = None
        self._project = None
        self._is_base_line = None
        self._type = None
        self._created_time = None
        self.discriminator = None

        if case_id is not None:
            self.case_id = case_id
        if case_num is not None:
            self.case_num = case_num
        if case_name is not None:
            self.case_name = case_name
        if case_level is not None:
            self.case_level = case_level
        if status is not None:
            self.status = status
        if creator is not None:
            self.creator = creator
        if owner is not None:
            self.owner = owner
        if project is not None:
            self.project = project
        if is_base_line is not None:
            self.is_base_line = is_base_line
        if type is not None:
            self.type = type
        if created_time is not None:
            self.created_time = created_time

    @property
    def case_id(self):
        """Gets the case_id of this AssociatedTestCase.

        用例ID

        :return: The case_id of this AssociatedTestCase.
        :rtype: str
        """
        return self._case_id

    @case_id.setter
    def case_id(self, case_id):
        """Sets the case_id of this AssociatedTestCase.

        用例ID

        :param case_id: The case_id of this AssociatedTestCase.
        :type case_id: str
        """
        self._case_id = case_id

    @property
    def case_num(self):
        """Gets the case_num of this AssociatedTestCase.

        用例编号

        :return: The case_num of this AssociatedTestCase.
        :rtype: str
        """
        return self._case_num

    @case_num.setter
    def case_num(self, case_num):
        """Sets the case_num of this AssociatedTestCase.

        用例编号

        :param case_num: The case_num of this AssociatedTestCase.
        :type case_num: str
        """
        self._case_num = case_num

    @property
    def case_name(self):
        """Gets the case_name of this AssociatedTestCase.

        用例名称

        :return: The case_name of this AssociatedTestCase.
        :rtype: str
        """
        return self._case_name

    @case_name.setter
    def case_name(self, case_name):
        """Sets the case_name of this AssociatedTestCase.

        用例名称

        :param case_name: The case_name of this AssociatedTestCase.
        :type case_name: str
        """
        self._case_name = case_name

    @property
    def case_level(self):
        """Gets the case_level of this AssociatedTestCase.

        用例等级

        :return: The case_level of this AssociatedTestCase.
        :rtype: str
        """
        return self._case_level

    @case_level.setter
    def case_level(self, case_level):
        """Sets the case_level of this AssociatedTestCase.

        用例等级

        :param case_level: The case_level of this AssociatedTestCase.
        :type case_level: str
        """
        self._case_level = case_level

    @property
    def status(self):
        """Gets the status of this AssociatedTestCase.


        :return: The status of this AssociatedTestCase.
        :rtype: :class:`huaweicloudsdkprojectman.v4.StatusVo`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AssociatedTestCase.


        :param status: The status of this AssociatedTestCase.
        :type status: :class:`huaweicloudsdkprojectman.v4.StatusVo`
        """
        self._status = status

    @property
    def creator(self):
        """Gets the creator of this AssociatedTestCase.


        :return: The creator of this AssociatedTestCase.
        :rtype: :class:`huaweicloudsdkprojectman.v4.SimpleUser`
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this AssociatedTestCase.


        :param creator: The creator of this AssociatedTestCase.
        :type creator: :class:`huaweicloudsdkprojectman.v4.SimpleUser`
        """
        self._creator = creator

    @property
    def owner(self):
        """Gets the owner of this AssociatedTestCase.


        :return: The owner of this AssociatedTestCase.
        :rtype: :class:`huaweicloudsdkprojectman.v4.SimpleUser`
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this AssociatedTestCase.


        :param owner: The owner of this AssociatedTestCase.
        :type owner: :class:`huaweicloudsdkprojectman.v4.SimpleUser`
        """
        self._owner = owner

    @property
    def project(self):
        """Gets the project of this AssociatedTestCase.


        :return: The project of this AssociatedTestCase.
        :rtype: :class:`huaweicloudsdkprojectman.v4.SimpleProject`
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this AssociatedTestCase.


        :param project: The project of this AssociatedTestCase.
        :type project: :class:`huaweicloudsdkprojectman.v4.SimpleProject`
        """
        self._project = project

    @property
    def is_base_line(self):
        """Gets the is_base_line of this AssociatedTestCase.

        是否基线

        :return: The is_base_line of this AssociatedTestCase.
        :rtype: int
        """
        return self._is_base_line

    @is_base_line.setter
    def is_base_line(self, is_base_line):
        """Sets the is_base_line of this AssociatedTestCase.

        是否基线

        :param is_base_line: The is_base_line of this AssociatedTestCase.
        :type is_base_line: int
        """
        self._is_base_line = is_base_line

    @property
    def type(self):
        """Gets the type of this AssociatedTestCase.

        用例类型

        :return: The type of this AssociatedTestCase.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AssociatedTestCase.

        用例类型

        :param type: The type of this AssociatedTestCase.
        :type type: str
        """
        self._type = type

    @property
    def created_time(self):
        """Gets the created_time of this AssociatedTestCase.

        创建时间

        :return: The created_time of this AssociatedTestCase.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this AssociatedTestCase.

        创建时间

        :param created_time: The created_time of this AssociatedTestCase.
        :type created_time: int
        """
        self._created_time = created_time

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
        if not isinstance(other, AssociatedTestCase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

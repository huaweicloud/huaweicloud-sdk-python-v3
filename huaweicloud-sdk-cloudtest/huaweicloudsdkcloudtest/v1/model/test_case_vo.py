# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestCaseVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uri': 'str',
        'number': 'str',
        'name': 'str',
        'dr_relation_id': 'str',
        'status_code': 'str',
        'status_name': 'str',
        'author': 'str',
        'author_id': 'str',
        'owner': 'str',
        'project_uuid': 'str',
        'creation_date': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'number': 'number',
        'name': 'name',
        'dr_relation_id': 'dr_relation_id',
        'status_code': 'status_code',
        'status_name': 'status_name',
        'author': 'author',
        'author_id': 'author_id',
        'owner': 'owner',
        'project_uuid': 'project_uuid',
        'creation_date': 'creation_date'
    }

    def __init__(self, uri=None, number=None, name=None, dr_relation_id=None, status_code=None, status_name=None, author=None, author_id=None, owner=None, project_uuid=None, creation_date=None):
        """TestCaseVo

        The model defined in huaweicloud sdk

        :param uri: 用例ID
        :type uri: str
        :param number: 用例编号
        :type number: str
        :param name: 用例名称
        :type name: str
        :param dr_relation_id: 工作项id
        :type dr_relation_id: str
        :param status_code: 状态ID
        :type status_code: str
        :param status_name: 状态名称
        :type status_name: str
        :param author: 创建人名称
        :type author: str
        :param author_id: 创建人ID
        :type author_id: str
        :param owner: 处理人名称
        :type owner: str
        :param project_uuid: 项目ID
        :type project_uuid: str
        :param creation_date: 创建时间
        :type creation_date: str
        """
        
        

        self._uri = None
        self._number = None
        self._name = None
        self._dr_relation_id = None
        self._status_code = None
        self._status_name = None
        self._author = None
        self._author_id = None
        self._owner = None
        self._project_uuid = None
        self._creation_date = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if number is not None:
            self.number = number
        if name is not None:
            self.name = name
        if dr_relation_id is not None:
            self.dr_relation_id = dr_relation_id
        if status_code is not None:
            self.status_code = status_code
        if status_name is not None:
            self.status_name = status_name
        if author is not None:
            self.author = author
        if author_id is not None:
            self.author_id = author_id
        if owner is not None:
            self.owner = owner
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if creation_date is not None:
            self.creation_date = creation_date

    @property
    def uri(self):
        """Gets the uri of this TestCaseVo.

        用例ID

        :return: The uri of this TestCaseVo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this TestCaseVo.

        用例ID

        :param uri: The uri of this TestCaseVo.
        :type uri: str
        """
        self._uri = uri

    @property
    def number(self):
        """Gets the number of this TestCaseVo.

        用例编号

        :return: The number of this TestCaseVo.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this TestCaseVo.

        用例编号

        :param number: The number of this TestCaseVo.
        :type number: str
        """
        self._number = number

    @property
    def name(self):
        """Gets the name of this TestCaseVo.

        用例名称

        :return: The name of this TestCaseVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TestCaseVo.

        用例名称

        :param name: The name of this TestCaseVo.
        :type name: str
        """
        self._name = name

    @property
    def dr_relation_id(self):
        """Gets the dr_relation_id of this TestCaseVo.

        工作项id

        :return: The dr_relation_id of this TestCaseVo.
        :rtype: str
        """
        return self._dr_relation_id

    @dr_relation_id.setter
    def dr_relation_id(self, dr_relation_id):
        """Sets the dr_relation_id of this TestCaseVo.

        工作项id

        :param dr_relation_id: The dr_relation_id of this TestCaseVo.
        :type dr_relation_id: str
        """
        self._dr_relation_id = dr_relation_id

    @property
    def status_code(self):
        """Gets the status_code of this TestCaseVo.

        状态ID

        :return: The status_code of this TestCaseVo.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this TestCaseVo.

        状态ID

        :param status_code: The status_code of this TestCaseVo.
        :type status_code: str
        """
        self._status_code = status_code

    @property
    def status_name(self):
        """Gets the status_name of this TestCaseVo.

        状态名称

        :return: The status_name of this TestCaseVo.
        :rtype: str
        """
        return self._status_name

    @status_name.setter
    def status_name(self, status_name):
        """Sets the status_name of this TestCaseVo.

        状态名称

        :param status_name: The status_name of this TestCaseVo.
        :type status_name: str
        """
        self._status_name = status_name

    @property
    def author(self):
        """Gets the author of this TestCaseVo.

        创建人名称

        :return: The author of this TestCaseVo.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this TestCaseVo.

        创建人名称

        :param author: The author of this TestCaseVo.
        :type author: str
        """
        self._author = author

    @property
    def author_id(self):
        """Gets the author_id of this TestCaseVo.

        创建人ID

        :return: The author_id of this TestCaseVo.
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this TestCaseVo.

        创建人ID

        :param author_id: The author_id of this TestCaseVo.
        :type author_id: str
        """
        self._author_id = author_id

    @property
    def owner(self):
        """Gets the owner of this TestCaseVo.

        处理人名称

        :return: The owner of this TestCaseVo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this TestCaseVo.

        处理人名称

        :param owner: The owner of this TestCaseVo.
        :type owner: str
        """
        self._owner = owner

    @property
    def project_uuid(self):
        """Gets the project_uuid of this TestCaseVo.

        项目ID

        :return: The project_uuid of this TestCaseVo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this TestCaseVo.

        项目ID

        :param project_uuid: The project_uuid of this TestCaseVo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def creation_date(self):
        """Gets the creation_date of this TestCaseVo.

        创建时间

        :return: The creation_date of this TestCaseVo.
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this TestCaseVo.

        创建时间

        :param creation_date: The creation_date of this TestCaseVo.
        :type creation_date: str
        """
        self._creation_date = creation_date

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
        if not isinstance(other, TestCaseVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

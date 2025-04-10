# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectFieldConfigOptionVo:

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
        'name': 'str',
        'code': 'str',
        'updator': 'NameAndIdVo',
        'description': 'str',
        'flag': 'int',
        'sort_numb': 'int',
        'creator': 'NameAndIdVo',
        'create_time_stamp': 'int',
        'update_time_stamp': 'int'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'code': 'code',
        'updator': 'updator',
        'description': 'description',
        'flag': 'flag',
        'sort_numb': 'sort_numb',
        'creator': 'creator',
        'create_time_stamp': 'create_time_stamp',
        'update_time_stamp': 'update_time_stamp'
    }

    def __init__(self, uri=None, name=None, code=None, updator=None, description=None, flag=None, sort_numb=None, creator=None, create_time_stamp=None, update_time_stamp=None):
        r"""ProjectFieldConfigOptionVo

        The model defined in huaweicloud sdk

        :param uri: 字段选项URI标识.新增不传，修改、删除使用必传
        :type uri: str
        :param name: 可选项名称
        :type name: str
        :param code: 可选项code值
        :type code: str
        :param updator: 
        :type updator: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        :param description: 描述
        :type description: str
        :param flag: 修改标识，0：不可修改 1：可修改，用于结果和状态的选项值
        :type flag: int
        :param sort_numb: 顺序数值
        :type sort_numb: int
        :param creator: 
        :type creator: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        :param create_time_stamp: 创建时间时间戳
        :type create_time_stamp: int
        :param update_time_stamp: 更新时间时间戳
        :type update_time_stamp: int
        """
        
        

        self._uri = None
        self._name = None
        self._code = None
        self._updator = None
        self._description = None
        self._flag = None
        self._sort_numb = None
        self._creator = None
        self._create_time_stamp = None
        self._update_time_stamp = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if updator is not None:
            self.updator = updator
        if description is not None:
            self.description = description
        if flag is not None:
            self.flag = flag
        if sort_numb is not None:
            self.sort_numb = sort_numb
        if creator is not None:
            self.creator = creator
        if create_time_stamp is not None:
            self.create_time_stamp = create_time_stamp
        if update_time_stamp is not None:
            self.update_time_stamp = update_time_stamp

    @property
    def uri(self):
        r"""Gets the uri of this ProjectFieldConfigOptionVo.

        字段选项URI标识.新增不传，修改、删除使用必传

        :return: The uri of this ProjectFieldConfigOptionVo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this ProjectFieldConfigOptionVo.

        字段选项URI标识.新增不传，修改、删除使用必传

        :param uri: The uri of this ProjectFieldConfigOptionVo.
        :type uri: str
        """
        self._uri = uri

    @property
    def name(self):
        r"""Gets the name of this ProjectFieldConfigOptionVo.

        可选项名称

        :return: The name of this ProjectFieldConfigOptionVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ProjectFieldConfigOptionVo.

        可选项名称

        :param name: The name of this ProjectFieldConfigOptionVo.
        :type name: str
        """
        self._name = name

    @property
    def code(self):
        r"""Gets the code of this ProjectFieldConfigOptionVo.

        可选项code值

        :return: The code of this ProjectFieldConfigOptionVo.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ProjectFieldConfigOptionVo.

        可选项code值

        :param code: The code of this ProjectFieldConfigOptionVo.
        :type code: str
        """
        self._code = code

    @property
    def updator(self):
        r"""Gets the updator of this ProjectFieldConfigOptionVo.

        :return: The updator of this ProjectFieldConfigOptionVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        return self._updator

    @updator.setter
    def updator(self, updator):
        r"""Sets the updator of this ProjectFieldConfigOptionVo.

        :param updator: The updator of this ProjectFieldConfigOptionVo.
        :type updator: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        self._updator = updator

    @property
    def description(self):
        r"""Gets the description of this ProjectFieldConfigOptionVo.

        描述

        :return: The description of this ProjectFieldConfigOptionVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ProjectFieldConfigOptionVo.

        描述

        :param description: The description of this ProjectFieldConfigOptionVo.
        :type description: str
        """
        self._description = description

    @property
    def flag(self):
        r"""Gets the flag of this ProjectFieldConfigOptionVo.

        修改标识，0：不可修改 1：可修改，用于结果和状态的选项值

        :return: The flag of this ProjectFieldConfigOptionVo.
        :rtype: int
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        r"""Sets the flag of this ProjectFieldConfigOptionVo.

        修改标识，0：不可修改 1：可修改，用于结果和状态的选项值

        :param flag: The flag of this ProjectFieldConfigOptionVo.
        :type flag: int
        """
        self._flag = flag

    @property
    def sort_numb(self):
        r"""Gets the sort_numb of this ProjectFieldConfigOptionVo.

        顺序数值

        :return: The sort_numb of this ProjectFieldConfigOptionVo.
        :rtype: int
        """
        return self._sort_numb

    @sort_numb.setter
    def sort_numb(self, sort_numb):
        r"""Sets the sort_numb of this ProjectFieldConfigOptionVo.

        顺序数值

        :param sort_numb: The sort_numb of this ProjectFieldConfigOptionVo.
        :type sort_numb: int
        """
        self._sort_numb = sort_numb

    @property
    def creator(self):
        r"""Gets the creator of this ProjectFieldConfigOptionVo.

        :return: The creator of this ProjectFieldConfigOptionVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ProjectFieldConfigOptionVo.

        :param creator: The creator of this ProjectFieldConfigOptionVo.
        :type creator: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        self._creator = creator

    @property
    def create_time_stamp(self):
        r"""Gets the create_time_stamp of this ProjectFieldConfigOptionVo.

        创建时间时间戳

        :return: The create_time_stamp of this ProjectFieldConfigOptionVo.
        :rtype: int
        """
        return self._create_time_stamp

    @create_time_stamp.setter
    def create_time_stamp(self, create_time_stamp):
        r"""Sets the create_time_stamp of this ProjectFieldConfigOptionVo.

        创建时间时间戳

        :param create_time_stamp: The create_time_stamp of this ProjectFieldConfigOptionVo.
        :type create_time_stamp: int
        """
        self._create_time_stamp = create_time_stamp

    @property
    def update_time_stamp(self):
        r"""Gets the update_time_stamp of this ProjectFieldConfigOptionVo.

        更新时间时间戳

        :return: The update_time_stamp of this ProjectFieldConfigOptionVo.
        :rtype: int
        """
        return self._update_time_stamp

    @update_time_stamp.setter
    def update_time_stamp(self, update_time_stamp):
        r"""Sets the update_time_stamp of this ProjectFieldConfigOptionVo.

        更新时间时间戳

        :param update_time_stamp: The update_time_stamp of this ProjectFieldConfigOptionVo.
        :type update_time_stamp: int
        """
        self._update_time_stamp = update_time_stamp

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
        if not isinstance(other, ProjectFieldConfigOptionVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

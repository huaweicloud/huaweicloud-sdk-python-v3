# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CmAttributeVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'default_attr_name_cn': 'str',
        'default_attr_name_en': 'str',
        'cust_attr_name': 'str',
        'status': 'int',
        'create_time': 'datetime',
        'modify_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'default_attr_name_cn': 'default_attr_name_cn',
        'default_attr_name_en': 'default_attr_name_en',
        'cust_attr_name': 'cust_attr_name',
        'status': 'status',
        'create_time': 'create_time',
        'modify_time': 'modify_time'
    }

    def __init__(self, id=None, default_attr_name_cn=None, default_attr_name_en=None, cust_attr_name=None, status=None, create_time=None, modify_time=None):
        """CmAttributeVO

        The model defined in huaweicloud sdk

        :param id: 自定义属性标识
        :type id: int
        :param default_attr_name_cn: 默认属性名称中文
        :type default_attr_name_cn: str
        :param default_attr_name_en: 默认属性名称英文
        :type default_attr_name_en: str
        :param cust_attr_name: 自定义属性名称
        :type cust_attr_name: str
        :param status: 自定义属性状态：0 未启用，1 已启用。
        :type status: int
        :param create_time: 创建时间
        :type create_time: datetime
        :param modify_time: 更新时间
        :type modify_time: datetime
        """
        
        

        self._id = None
        self._default_attr_name_cn = None
        self._default_attr_name_en = None
        self._cust_attr_name = None
        self._status = None
        self._create_time = None
        self._modify_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if default_attr_name_cn is not None:
            self.default_attr_name_cn = default_attr_name_cn
        if default_attr_name_en is not None:
            self.default_attr_name_en = default_attr_name_en
        if cust_attr_name is not None:
            self.cust_attr_name = cust_attr_name
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if modify_time is not None:
            self.modify_time = modify_time

    @property
    def id(self):
        """Gets the id of this CmAttributeVO.

        自定义属性标识

        :return: The id of this CmAttributeVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CmAttributeVO.

        自定义属性标识

        :param id: The id of this CmAttributeVO.
        :type id: int
        """
        self._id = id

    @property
    def default_attr_name_cn(self):
        """Gets the default_attr_name_cn of this CmAttributeVO.

        默认属性名称中文

        :return: The default_attr_name_cn of this CmAttributeVO.
        :rtype: str
        """
        return self._default_attr_name_cn

    @default_attr_name_cn.setter
    def default_attr_name_cn(self, default_attr_name_cn):
        """Sets the default_attr_name_cn of this CmAttributeVO.

        默认属性名称中文

        :param default_attr_name_cn: The default_attr_name_cn of this CmAttributeVO.
        :type default_attr_name_cn: str
        """
        self._default_attr_name_cn = default_attr_name_cn

    @property
    def default_attr_name_en(self):
        """Gets the default_attr_name_en of this CmAttributeVO.

        默认属性名称英文

        :return: The default_attr_name_en of this CmAttributeVO.
        :rtype: str
        """
        return self._default_attr_name_en

    @default_attr_name_en.setter
    def default_attr_name_en(self, default_attr_name_en):
        """Sets the default_attr_name_en of this CmAttributeVO.

        默认属性名称英文

        :param default_attr_name_en: The default_attr_name_en of this CmAttributeVO.
        :type default_attr_name_en: str
        """
        self._default_attr_name_en = default_attr_name_en

    @property
    def cust_attr_name(self):
        """Gets the cust_attr_name of this CmAttributeVO.

        自定义属性名称

        :return: The cust_attr_name of this CmAttributeVO.
        :rtype: str
        """
        return self._cust_attr_name

    @cust_attr_name.setter
    def cust_attr_name(self, cust_attr_name):
        """Sets the cust_attr_name of this CmAttributeVO.

        自定义属性名称

        :param cust_attr_name: The cust_attr_name of this CmAttributeVO.
        :type cust_attr_name: str
        """
        self._cust_attr_name = cust_attr_name

    @property
    def status(self):
        """Gets the status of this CmAttributeVO.

        自定义属性状态：0 未启用，1 已启用。

        :return: The status of this CmAttributeVO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CmAttributeVO.

        自定义属性状态：0 未启用，1 已启用。

        :param status: The status of this CmAttributeVO.
        :type status: int
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this CmAttributeVO.

        创建时间

        :return: The create_time of this CmAttributeVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CmAttributeVO.

        创建时间

        :param create_time: The create_time of this CmAttributeVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def modify_time(self):
        """Gets the modify_time of this CmAttributeVO.

        更新时间

        :return: The modify_time of this CmAttributeVO.
        :rtype: datetime
        """
        return self._modify_time

    @modify_time.setter
    def modify_time(self, modify_time):
        """Sets the modify_time of this CmAttributeVO.

        更新时间

        :param modify_time: The modify_time of this CmAttributeVO.
        :type modify_time: datetime
        """
        self._modify_time = modify_time

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
        if not isinstance(other, CmAttributeVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelStatisticVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'biz_type': 'BizTypeEnum',
        'level': 'ModelLevel',
        'db': 'int',
        'tb': 'int',
        'tb_published': 'int',
        'fd': 'int',
        'fd_published': 'int',
        'st': 'float',
        'st_published': 'float',
        'model': 'WorkspaceVO'
    }

    attribute_map = {
        'biz_type': 'biz_type',
        'level': 'level',
        'db': 'db',
        'tb': 'tb',
        'tb_published': 'tb_published',
        'fd': 'fd',
        'fd_published': 'fd_published',
        'st': 'st',
        'st_published': 'st_published',
        'model': 'model'
    }

    def __init__(self, biz_type=None, level=None, db=None, tb=None, tb_published=None, fd=None, fd_published=None, st=None, st_published=None, model=None):
        r"""ModelStatisticVO

        The model defined in huaweicloud sdk

        :param biz_type: 
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        :param level: 
        :type level: :class:`huaweicloudsdkdataartsstudio.v1.ModelLevel`
        :param db: 数据库。
        :type db: int
        :param tb: 数据表。
        :type tb: int
        :param tb_published: 已发布的数据表。
        :type tb_published: int
        :param fd: 字段。
        :type fd: int
        :param fd_published: 已发布的字段。
        :type fd_published: int
        :param st: 标准覆盖率。
        :type st: float
        :param st_published: 已发布的标准覆盖率。
        :type st_published: float
        :param model: 
        :type model: :class:`huaweicloudsdkdataartsstudio.v1.WorkspaceVO`
        """
        
        

        self._biz_type = None
        self._level = None
        self._db = None
        self._tb = None
        self._tb_published = None
        self._fd = None
        self._fd_published = None
        self._st = None
        self._st_published = None
        self._model = None
        self.discriminator = None

        if biz_type is not None:
            self.biz_type = biz_type
        if level is not None:
            self.level = level
        if db is not None:
            self.db = db
        if tb is not None:
            self.tb = tb
        if tb_published is not None:
            self.tb_published = tb_published
        if fd is not None:
            self.fd = fd
        if fd_published is not None:
            self.fd_published = fd_published
        if st is not None:
            self.st = st
        if st_published is not None:
            self.st_published = st_published
        if model is not None:
            self.model = model

    @property
    def biz_type(self):
        r"""Gets the biz_type of this ModelStatisticVO.

        :return: The biz_type of this ModelStatisticVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        r"""Sets the biz_type of this ModelStatisticVO.

        :param biz_type: The biz_type of this ModelStatisticVO.
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        self._biz_type = biz_type

    @property
    def level(self):
        r"""Gets the level of this ModelStatisticVO.

        :return: The level of this ModelStatisticVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ModelLevel`
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ModelStatisticVO.

        :param level: The level of this ModelStatisticVO.
        :type level: :class:`huaweicloudsdkdataartsstudio.v1.ModelLevel`
        """
        self._level = level

    @property
    def db(self):
        r"""Gets the db of this ModelStatisticVO.

        数据库。

        :return: The db of this ModelStatisticVO.
        :rtype: int
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this ModelStatisticVO.

        数据库。

        :param db: The db of this ModelStatisticVO.
        :type db: int
        """
        self._db = db

    @property
    def tb(self):
        r"""Gets the tb of this ModelStatisticVO.

        数据表。

        :return: The tb of this ModelStatisticVO.
        :rtype: int
        """
        return self._tb

    @tb.setter
    def tb(self, tb):
        r"""Sets the tb of this ModelStatisticVO.

        数据表。

        :param tb: The tb of this ModelStatisticVO.
        :type tb: int
        """
        self._tb = tb

    @property
    def tb_published(self):
        r"""Gets the tb_published of this ModelStatisticVO.

        已发布的数据表。

        :return: The tb_published of this ModelStatisticVO.
        :rtype: int
        """
        return self._tb_published

    @tb_published.setter
    def tb_published(self, tb_published):
        r"""Sets the tb_published of this ModelStatisticVO.

        已发布的数据表。

        :param tb_published: The tb_published of this ModelStatisticVO.
        :type tb_published: int
        """
        self._tb_published = tb_published

    @property
    def fd(self):
        r"""Gets the fd of this ModelStatisticVO.

        字段。

        :return: The fd of this ModelStatisticVO.
        :rtype: int
        """
        return self._fd

    @fd.setter
    def fd(self, fd):
        r"""Sets the fd of this ModelStatisticVO.

        字段。

        :param fd: The fd of this ModelStatisticVO.
        :type fd: int
        """
        self._fd = fd

    @property
    def fd_published(self):
        r"""Gets the fd_published of this ModelStatisticVO.

        已发布的字段。

        :return: The fd_published of this ModelStatisticVO.
        :rtype: int
        """
        return self._fd_published

    @fd_published.setter
    def fd_published(self, fd_published):
        r"""Sets the fd_published of this ModelStatisticVO.

        已发布的字段。

        :param fd_published: The fd_published of this ModelStatisticVO.
        :type fd_published: int
        """
        self._fd_published = fd_published

    @property
    def st(self):
        r"""Gets the st of this ModelStatisticVO.

        标准覆盖率。

        :return: The st of this ModelStatisticVO.
        :rtype: float
        """
        return self._st

    @st.setter
    def st(self, st):
        r"""Sets the st of this ModelStatisticVO.

        标准覆盖率。

        :param st: The st of this ModelStatisticVO.
        :type st: float
        """
        self._st = st

    @property
    def st_published(self):
        r"""Gets the st_published of this ModelStatisticVO.

        已发布的标准覆盖率。

        :return: The st_published of this ModelStatisticVO.
        :rtype: float
        """
        return self._st_published

    @st_published.setter
    def st_published(self, st_published):
        r"""Sets the st_published of this ModelStatisticVO.

        已发布的标准覆盖率。

        :param st_published: The st_published of this ModelStatisticVO.
        :type st_published: float
        """
        self._st_published = st_published

    @property
    def model(self):
        r"""Gets the model of this ModelStatisticVO.

        :return: The model of this ModelStatisticVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.WorkspaceVO`
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this ModelStatisticVO.

        :param model: The model of this ModelStatisticVO.
        :type model: :class:`huaweicloudsdkdataartsstudio.v1.WorkspaceVO`
        """
        self._model = model

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
        if not isinstance(other, ModelStatisticVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

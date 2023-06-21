# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StandElementValueVOList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'values': 'list[StandElementValueVO]',
        'id': 'int',
        'directory_id': 'int',
        'directory_path': 'str',
        'row_id': 'int',
        'status': 'BizStatusEnum',
        'approval_info': 'ApprovalVO',
        'new_biz': 'BizVersionManageVO',
        'create_by': 'str',
        'update_by': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'values': 'values',
        'id': 'id',
        'directory_id': 'directory_id',
        'directory_path': 'directory_path',
        'row_id': 'row_id',
        'status': 'status',
        'approval_info': 'approval_info',
        'new_biz': 'new_biz',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, values=None, id=None, directory_id=None, directory_path=None, row_id=None, status=None, approval_info=None, new_biz=None, create_by=None, update_by=None, create_time=None, update_time=None):
        """StandElementValueVOList

        The model defined in huaweicloud sdk

        :param values: 属性信息
        :type values: list[:class:`huaweicloudsdkdataartsstudio.v1.StandElementValueVO`]
        :param id: ID
        :type id: int
        :param directory_id: 标准所属目录
        :type directory_id: int
        :param directory_path: 目录树
        :type directory_path: str
        :param row_id: 标准行的id
        :type row_id: int
        :param status: 
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        :param approval_info: 
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        :param new_biz: 
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        :param create_by: 创建人
        :type create_by: str
        :param update_by: 更新人
        :type update_by: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param update_time: 更新时间
        :type update_time: datetime
        """
        
        

        self._values = None
        self._id = None
        self._directory_id = None
        self._directory_path = None
        self._row_id = None
        self._status = None
        self._approval_info = None
        self._new_biz = None
        self._create_by = None
        self._update_by = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        self.values = values
        if id is not None:
            self.id = id
        self.directory_id = directory_id
        if directory_path is not None:
            self.directory_path = directory_path
        if row_id is not None:
            self.row_id = row_id
        if status is not None:
            self.status = status
        if approval_info is not None:
            self.approval_info = approval_info
        if new_biz is not None:
            self.new_biz = new_biz
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def values(self):
        """Gets the values of this StandElementValueVOList.

        属性信息

        :return: The values of this StandElementValueVOList.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.StandElementValueVO`]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this StandElementValueVOList.

        属性信息

        :param values: The values of this StandElementValueVOList.
        :type values: list[:class:`huaweicloudsdkdataartsstudio.v1.StandElementValueVO`]
        """
        self._values = values

    @property
    def id(self):
        """Gets the id of this StandElementValueVOList.

        ID

        :return: The id of this StandElementValueVOList.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StandElementValueVOList.

        ID

        :param id: The id of this StandElementValueVOList.
        :type id: int
        """
        self._id = id

    @property
    def directory_id(self):
        """Gets the directory_id of this StandElementValueVOList.

        标准所属目录

        :return: The directory_id of this StandElementValueVOList.
        :rtype: int
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        """Sets the directory_id of this StandElementValueVOList.

        标准所属目录

        :param directory_id: The directory_id of this StandElementValueVOList.
        :type directory_id: int
        """
        self._directory_id = directory_id

    @property
    def directory_path(self):
        """Gets the directory_path of this StandElementValueVOList.

        目录树

        :return: The directory_path of this StandElementValueVOList.
        :rtype: str
        """
        return self._directory_path

    @directory_path.setter
    def directory_path(self, directory_path):
        """Sets the directory_path of this StandElementValueVOList.

        目录树

        :param directory_path: The directory_path of this StandElementValueVOList.
        :type directory_path: str
        """
        self._directory_path = directory_path

    @property
    def row_id(self):
        """Gets the row_id of this StandElementValueVOList.

        标准行的id

        :return: The row_id of this StandElementValueVOList.
        :rtype: int
        """
        return self._row_id

    @row_id.setter
    def row_id(self, row_id):
        """Sets the row_id of this StandElementValueVOList.

        标准行的id

        :param row_id: The row_id of this StandElementValueVOList.
        :type row_id: int
        """
        self._row_id = row_id

    @property
    def status(self):
        """Gets the status of this StandElementValueVOList.

        :return: The status of this StandElementValueVOList.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StandElementValueVOList.

        :param status: The status of this StandElementValueVOList.
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        self._status = status

    @property
    def approval_info(self):
        """Gets the approval_info of this StandElementValueVOList.

        :return: The approval_info of this StandElementValueVOList.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        return self._approval_info

    @approval_info.setter
    def approval_info(self, approval_info):
        """Sets the approval_info of this StandElementValueVOList.

        :param approval_info: The approval_info of this StandElementValueVOList.
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        self._approval_info = approval_info

    @property
    def new_biz(self):
        """Gets the new_biz of this StandElementValueVOList.

        :return: The new_biz of this StandElementValueVOList.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        return self._new_biz

    @new_biz.setter
    def new_biz(self, new_biz):
        """Sets the new_biz of this StandElementValueVOList.

        :param new_biz: The new_biz of this StandElementValueVOList.
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        self._new_biz = new_biz

    @property
    def create_by(self):
        """Gets the create_by of this StandElementValueVOList.

        创建人

        :return: The create_by of this StandElementValueVOList.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this StandElementValueVOList.

        创建人

        :param create_by: The create_by of this StandElementValueVOList.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        """Gets the update_by of this StandElementValueVOList.

        更新人

        :return: The update_by of this StandElementValueVOList.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this StandElementValueVOList.

        更新人

        :param update_by: The update_by of this StandElementValueVOList.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def create_time(self):
        """Gets the create_time of this StandElementValueVOList.

        创建时间

        :return: The create_time of this StandElementValueVOList.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this StandElementValueVOList.

        创建时间

        :param create_time: The create_time of this StandElementValueVOList.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this StandElementValueVOList.

        更新时间

        :return: The update_time of this StandElementValueVOList.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this StandElementValueVOList.

        更新时间

        :param update_time: The update_time of this StandElementValueVOList.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, StandElementValueVOList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

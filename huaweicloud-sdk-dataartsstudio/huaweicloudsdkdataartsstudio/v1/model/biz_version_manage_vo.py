# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BizVersionManageVO:

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
        'biz_type': 'BizTypeEnum',
        'biz_id': 'int',
        'biz_info': 'str',
        'status': 'BizStatusEnum',
        'biz_version': 'int',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'biz_type': 'biz_type',
        'biz_id': 'biz_id',
        'biz_info': 'biz_info',
        'status': 'status',
        'biz_version': 'biz_version',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, biz_type=None, biz_id=None, biz_info=None, status=None, biz_version=None, create_time=None, update_time=None):
        """BizVersionManageVO

        The model defined in huaweicloud sdk

        :param id: ID信息
        :type id: int
        :param biz_type: 
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        :param biz_id: 业务id
        :type biz_id: int
        :param biz_info: 业务对象信息
        :type biz_info: str
        :param status: 
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        :param biz_version: 业务版本
        :type biz_version: int
        :param create_time: 创建时间
        :type create_time: datetime
        :param update_time: 更新时间
        :type update_time: datetime
        """
        
        

        self._id = None
        self._biz_type = None
        self._biz_id = None
        self._biz_info = None
        self._status = None
        self._biz_version = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if biz_type is not None:
            self.biz_type = biz_type
        if biz_id is not None:
            self.biz_id = biz_id
        if biz_info is not None:
            self.biz_info = biz_info
        if status is not None:
            self.status = status
        if biz_version is not None:
            self.biz_version = biz_version
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this BizVersionManageVO.

        ID信息

        :return: The id of this BizVersionManageVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BizVersionManageVO.

        ID信息

        :param id: The id of this BizVersionManageVO.
        :type id: int
        """
        self._id = id

    @property
    def biz_type(self):
        """Gets the biz_type of this BizVersionManageVO.

        :return: The biz_type of this BizVersionManageVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        """Sets the biz_type of this BizVersionManageVO.

        :param biz_type: The biz_type of this BizVersionManageVO.
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        self._biz_type = biz_type

    @property
    def biz_id(self):
        """Gets the biz_id of this BizVersionManageVO.

        业务id

        :return: The biz_id of this BizVersionManageVO.
        :rtype: int
        """
        return self._biz_id

    @biz_id.setter
    def biz_id(self, biz_id):
        """Sets the biz_id of this BizVersionManageVO.

        业务id

        :param biz_id: The biz_id of this BizVersionManageVO.
        :type biz_id: int
        """
        self._biz_id = biz_id

    @property
    def biz_info(self):
        """Gets the biz_info of this BizVersionManageVO.

        业务对象信息

        :return: The biz_info of this BizVersionManageVO.
        :rtype: str
        """
        return self._biz_info

    @biz_info.setter
    def biz_info(self, biz_info):
        """Sets the biz_info of this BizVersionManageVO.

        业务对象信息

        :param biz_info: The biz_info of this BizVersionManageVO.
        :type biz_info: str
        """
        self._biz_info = biz_info

    @property
    def status(self):
        """Gets the status of this BizVersionManageVO.

        :return: The status of this BizVersionManageVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BizVersionManageVO.

        :param status: The status of this BizVersionManageVO.
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        self._status = status

    @property
    def biz_version(self):
        """Gets the biz_version of this BizVersionManageVO.

        业务版本

        :return: The biz_version of this BizVersionManageVO.
        :rtype: int
        """
        return self._biz_version

    @biz_version.setter
    def biz_version(self, biz_version):
        """Sets the biz_version of this BizVersionManageVO.

        业务版本

        :param biz_version: The biz_version of this BizVersionManageVO.
        :type biz_version: int
        """
        self._biz_version = biz_version

    @property
    def create_time(self):
        """Gets the create_time of this BizVersionManageVO.

        创建时间

        :return: The create_time of this BizVersionManageVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this BizVersionManageVO.

        创建时间

        :param create_time: The create_time of this BizVersionManageVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this BizVersionManageVO.

        更新时间

        :return: The update_time of this BizVersionManageVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this BizVersionManageVO.

        更新时间

        :param update_time: The update_time of this BizVersionManageVO.
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
        if not isinstance(other, BizVersionManageVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

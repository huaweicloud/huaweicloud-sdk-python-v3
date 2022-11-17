# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCompetitionWorksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'competition_id': 'int',
        'stage_id': 'int',
        'read_time': 'str',
        'time_unit': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'competition_id': 'competition_id',
        'stage_id': 'stage_id',
        'read_time': 'read_time',
        'time_unit': 'time_unit',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, competition_id=None, stage_id=None, read_time=None, time_unit=None, offset=None, limit=None, sort_key=None, sort_dir=None):
        """ListCompetitionWorksRequest

        The model defined in huaweicloud sdk

        :param competition_id: 要查询的大赛ID，由大赛平台提供
        :type competition_id: int
        :param stage_id: 要查询的大赛阶段ID，由大赛平台提供
        :type stage_id: int
        :param read_time: 查询的截止时间
        :type read_time: str
        :param time_unit: 查询的时间范围。day表示以read_time作为结束时间,前一天内作为查询范围,hour表示以read_time作为结束时间,前一小内时作为查询范围。
        :type time_unit: str
        :param offset: 作品记录的起始编号,如果不传默认从0开始,offset为0时表示从第一条记录开始
        :type offset: int
        :param limit: 每页包含的作品记录数,如果不传默认返回100条，并且返回最大条数为100
        :type limit: int
        :param sort_key: 需要排序的字段，只支持works_id字段,如果不传则不进行排序
        :type sort_key: str
        :param sort_dir: 排序类型，支持asc|desc，默认为asc升序
        :type sort_dir: str
        """
        
        

        self._competition_id = None
        self._stage_id = None
        self._read_time = None
        self._time_unit = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.competition_id = competition_id
        self.stage_id = stage_id
        self.read_time = read_time
        if time_unit is not None:
            self.time_unit = time_unit
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def competition_id(self):
        """Gets the competition_id of this ListCompetitionWorksRequest.

        要查询的大赛ID，由大赛平台提供

        :return: The competition_id of this ListCompetitionWorksRequest.
        :rtype: int
        """
        return self._competition_id

    @competition_id.setter
    def competition_id(self, competition_id):
        """Sets the competition_id of this ListCompetitionWorksRequest.

        要查询的大赛ID，由大赛平台提供

        :param competition_id: The competition_id of this ListCompetitionWorksRequest.
        :type competition_id: int
        """
        self._competition_id = competition_id

    @property
    def stage_id(self):
        """Gets the stage_id of this ListCompetitionWorksRequest.

        要查询的大赛阶段ID，由大赛平台提供

        :return: The stage_id of this ListCompetitionWorksRequest.
        :rtype: int
        """
        return self._stage_id

    @stage_id.setter
    def stage_id(self, stage_id):
        """Sets the stage_id of this ListCompetitionWorksRequest.

        要查询的大赛阶段ID，由大赛平台提供

        :param stage_id: The stage_id of this ListCompetitionWorksRequest.
        :type stage_id: int
        """
        self._stage_id = stage_id

    @property
    def read_time(self):
        """Gets the read_time of this ListCompetitionWorksRequest.

        查询的截止时间

        :return: The read_time of this ListCompetitionWorksRequest.
        :rtype: str
        """
        return self._read_time

    @read_time.setter
    def read_time(self, read_time):
        """Sets the read_time of this ListCompetitionWorksRequest.

        查询的截止时间

        :param read_time: The read_time of this ListCompetitionWorksRequest.
        :type read_time: str
        """
        self._read_time = read_time

    @property
    def time_unit(self):
        """Gets the time_unit of this ListCompetitionWorksRequest.

        查询的时间范围。day表示以read_time作为结束时间,前一天内作为查询范围,hour表示以read_time作为结束时间,前一小内时作为查询范围。

        :return: The time_unit of this ListCompetitionWorksRequest.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """Sets the time_unit of this ListCompetitionWorksRequest.

        查询的时间范围。day表示以read_time作为结束时间,前一天内作为查询范围,hour表示以read_time作为结束时间,前一小内时作为查询范围。

        :param time_unit: The time_unit of this ListCompetitionWorksRequest.
        :type time_unit: str
        """
        self._time_unit = time_unit

    @property
    def offset(self):
        """Gets the offset of this ListCompetitionWorksRequest.

        作品记录的起始编号,如果不传默认从0开始,offset为0时表示从第一条记录开始

        :return: The offset of this ListCompetitionWorksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCompetitionWorksRequest.

        作品记录的起始编号,如果不传默认从0开始,offset为0时表示从第一条记录开始

        :param offset: The offset of this ListCompetitionWorksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListCompetitionWorksRequest.

        每页包含的作品记录数,如果不传默认返回100条，并且返回最大条数为100

        :return: The limit of this ListCompetitionWorksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCompetitionWorksRequest.

        每页包含的作品记录数,如果不传默认返回100条，并且返回最大条数为100

        :param limit: The limit of this ListCompetitionWorksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        """Gets the sort_key of this ListCompetitionWorksRequest.

        需要排序的字段，只支持works_id字段,如果不传则不进行排序

        :return: The sort_key of this ListCompetitionWorksRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListCompetitionWorksRequest.

        需要排序的字段，只支持works_id字段,如果不传则不进行排序

        :param sort_key: The sort_key of this ListCompetitionWorksRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListCompetitionWorksRequest.

        排序类型，支持asc|desc，默认为asc升序

        :return: The sort_dir of this ListCompetitionWorksRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListCompetitionWorksRequest.

        排序类型，支持asc|desc，默认为asc升序

        :param sort_dir: The sort_dir of this ListCompetitionWorksRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListCompetitionWorksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

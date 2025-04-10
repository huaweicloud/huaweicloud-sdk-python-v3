# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InterruptRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'sources': 'str',
        'sources_id': 'str',
        'sources_name': 'str',
        'region': 'str',
        'unavailable_start_time': 'int',
        'unavailable_end_time': 'int',
        'descriptions': 'str',
        'creator_id': 'str',
        'creator': 'str',
        'modified_id': 'str',
        'modified_by': 'str',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'sources': 'sources',
        'sources_id': 'sources_id',
        'sources_name': 'sources_name',
        'region': 'region',
        'unavailable_start_time': 'unavailable_start_time',
        'unavailable_end_time': 'unavailable_end_time',
        'descriptions': 'descriptions',
        'creator_id': 'creator_id',
        'creator': 'creator',
        'modified_id': 'modified_id',
        'modified_by': 'modified_by',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, sources=None, sources_id=None, sources_name=None, region=None, unavailable_start_time=None, unavailable_end_time=None, descriptions=None, creator_id=None, creator=None, modified_id=None, modified_by=None, create_time=None, update_time=None):
        r"""InterruptRecord

        The model defined in huaweicloud sdk

        :param id: 记录ID
        :type id: str
        :param sources: 来源 SLI SLI指标 WARROOM warroom ALERTS 告警 MALFUNCTIONS 故障 OTHERS 其他
        :type sources: str
        :param sources_id: 来源ID
        :type sources_id: str
        :param sources_name: 来源名称
        :type sources_name: str
        :param region: region
        :type region: str
        :param unavailable_start_time: 不可用开始时间
        :type unavailable_start_time: int
        :param unavailable_end_time: 不可用结束时间
        :type unavailable_end_time: int
        :param descriptions: 描述
        :type descriptions: str
        :param creator_id: 创建人Id
        :type creator_id: str
        :param creator: 创建人
        :type creator: str
        :param modified_id: 修改人ID
        :type modified_id: str
        :param modified_by: 修改人
        :type modified_by: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 修改时间
        :type update_time: int
        """
        
        

        self._id = None
        self._sources = None
        self._sources_id = None
        self._sources_name = None
        self._region = None
        self._unavailable_start_time = None
        self._unavailable_end_time = None
        self._descriptions = None
        self._creator_id = None
        self._creator = None
        self._modified_id = None
        self._modified_by = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if sources is not None:
            self.sources = sources
        if sources_id is not None:
            self.sources_id = sources_id
        if sources_name is not None:
            self.sources_name = sources_name
        if region is not None:
            self.region = region
        if unavailable_start_time is not None:
            self.unavailable_start_time = unavailable_start_time
        if unavailable_end_time is not None:
            self.unavailable_end_time = unavailable_end_time
        if descriptions is not None:
            self.descriptions = descriptions
        if creator_id is not None:
            self.creator_id = creator_id
        if creator is not None:
            self.creator = creator
        if modified_id is not None:
            self.modified_id = modified_id
        if modified_by is not None:
            self.modified_by = modified_by
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this InterruptRecord.

        记录ID

        :return: The id of this InterruptRecord.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InterruptRecord.

        记录ID

        :param id: The id of this InterruptRecord.
        :type id: str
        """
        self._id = id

    @property
    def sources(self):
        r"""Gets the sources of this InterruptRecord.

        来源 SLI SLI指标 WARROOM warroom ALERTS 告警 MALFUNCTIONS 故障 OTHERS 其他

        :return: The sources of this InterruptRecord.
        :rtype: str
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        r"""Sets the sources of this InterruptRecord.

        来源 SLI SLI指标 WARROOM warroom ALERTS 告警 MALFUNCTIONS 故障 OTHERS 其他

        :param sources: The sources of this InterruptRecord.
        :type sources: str
        """
        self._sources = sources

    @property
    def sources_id(self):
        r"""Gets the sources_id of this InterruptRecord.

        来源ID

        :return: The sources_id of this InterruptRecord.
        :rtype: str
        """
        return self._sources_id

    @sources_id.setter
    def sources_id(self, sources_id):
        r"""Sets the sources_id of this InterruptRecord.

        来源ID

        :param sources_id: The sources_id of this InterruptRecord.
        :type sources_id: str
        """
        self._sources_id = sources_id

    @property
    def sources_name(self):
        r"""Gets the sources_name of this InterruptRecord.

        来源名称

        :return: The sources_name of this InterruptRecord.
        :rtype: str
        """
        return self._sources_name

    @sources_name.setter
    def sources_name(self, sources_name):
        r"""Sets the sources_name of this InterruptRecord.

        来源名称

        :param sources_name: The sources_name of this InterruptRecord.
        :type sources_name: str
        """
        self._sources_name = sources_name

    @property
    def region(self):
        r"""Gets the region of this InterruptRecord.

        region

        :return: The region of this InterruptRecord.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this InterruptRecord.

        region

        :param region: The region of this InterruptRecord.
        :type region: str
        """
        self._region = region

    @property
    def unavailable_start_time(self):
        r"""Gets the unavailable_start_time of this InterruptRecord.

        不可用开始时间

        :return: The unavailable_start_time of this InterruptRecord.
        :rtype: int
        """
        return self._unavailable_start_time

    @unavailable_start_time.setter
    def unavailable_start_time(self, unavailable_start_time):
        r"""Sets the unavailable_start_time of this InterruptRecord.

        不可用开始时间

        :param unavailable_start_time: The unavailable_start_time of this InterruptRecord.
        :type unavailable_start_time: int
        """
        self._unavailable_start_time = unavailable_start_time

    @property
    def unavailable_end_time(self):
        r"""Gets the unavailable_end_time of this InterruptRecord.

        不可用结束时间

        :return: The unavailable_end_time of this InterruptRecord.
        :rtype: int
        """
        return self._unavailable_end_time

    @unavailable_end_time.setter
    def unavailable_end_time(self, unavailable_end_time):
        r"""Sets the unavailable_end_time of this InterruptRecord.

        不可用结束时间

        :param unavailable_end_time: The unavailable_end_time of this InterruptRecord.
        :type unavailable_end_time: int
        """
        self._unavailable_end_time = unavailable_end_time

    @property
    def descriptions(self):
        r"""Gets the descriptions of this InterruptRecord.

        描述

        :return: The descriptions of this InterruptRecord.
        :rtype: str
        """
        return self._descriptions

    @descriptions.setter
    def descriptions(self, descriptions):
        r"""Sets the descriptions of this InterruptRecord.

        描述

        :param descriptions: The descriptions of this InterruptRecord.
        :type descriptions: str
        """
        self._descriptions = descriptions

    @property
    def creator_id(self):
        r"""Gets the creator_id of this InterruptRecord.

        创建人Id

        :return: The creator_id of this InterruptRecord.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this InterruptRecord.

        创建人Id

        :param creator_id: The creator_id of this InterruptRecord.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator(self):
        r"""Gets the creator of this InterruptRecord.

        创建人

        :return: The creator of this InterruptRecord.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this InterruptRecord.

        创建人

        :param creator: The creator of this InterruptRecord.
        :type creator: str
        """
        self._creator = creator

    @property
    def modified_id(self):
        r"""Gets the modified_id of this InterruptRecord.

        修改人ID

        :return: The modified_id of this InterruptRecord.
        :rtype: str
        """
        return self._modified_id

    @modified_id.setter
    def modified_id(self, modified_id):
        r"""Sets the modified_id of this InterruptRecord.

        修改人ID

        :param modified_id: The modified_id of this InterruptRecord.
        :type modified_id: str
        """
        self._modified_id = modified_id

    @property
    def modified_by(self):
        r"""Gets the modified_by of this InterruptRecord.

        修改人

        :return: The modified_by of this InterruptRecord.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this InterruptRecord.

        修改人

        :param modified_by: The modified_by of this InterruptRecord.
        :type modified_by: str
        """
        self._modified_by = modified_by

    @property
    def create_time(self):
        r"""Gets the create_time of this InterruptRecord.

        创建时间

        :return: The create_time of this InterruptRecord.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this InterruptRecord.

        创建时间

        :param create_time: The create_time of this InterruptRecord.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this InterruptRecord.

        修改时间

        :return: The update_time of this InterruptRecord.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this InterruptRecord.

        修改时间

        :param update_time: The update_time of this InterruptRecord.
        :type update_time: int
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
        if not isinstance(other, InterruptRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

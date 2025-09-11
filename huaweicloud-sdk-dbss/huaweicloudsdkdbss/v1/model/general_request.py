# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GeneralRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_id': 'str',
        'regenerate': 'int',
        'time': 'Duration'
    }

    attribute_map = {
        'db_id': 'db_id',
        'regenerate': 'regenerate',
        'time': 'time'
    }

    def __init__(self, db_id=None, regenerate=None, time=None):
        r"""GeneralRequest

        The model defined in huaweicloud sdk

        :param db_id: 数据库ID
        :type db_id: str
        :param regenerate: 是否重新生成  - 1：是  - 0：否
        :type regenerate: int
        :param time: 
        :type time: :class:`huaweicloudsdkdbss.v1.Duration`
        """
        
        

        self._db_id = None
        self._regenerate = None
        self._time = None
        self.discriminator = None

        if db_id is not None:
            self.db_id = db_id
        self.regenerate = regenerate
        self.time = time

    @property
    def db_id(self):
        r"""Gets the db_id of this GeneralRequest.

        数据库ID

        :return: The db_id of this GeneralRequest.
        :rtype: str
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        r"""Sets the db_id of this GeneralRequest.

        数据库ID

        :param db_id: The db_id of this GeneralRequest.
        :type db_id: str
        """
        self._db_id = db_id

    @property
    def regenerate(self):
        r"""Gets the regenerate of this GeneralRequest.

        是否重新生成  - 1：是  - 0：否

        :return: The regenerate of this GeneralRequest.
        :rtype: int
        """
        return self._regenerate

    @regenerate.setter
    def regenerate(self, regenerate):
        r"""Sets the regenerate of this GeneralRequest.

        是否重新生成  - 1：是  - 0：否

        :param regenerate: The regenerate of this GeneralRequest.
        :type regenerate: int
        """
        self._regenerate = regenerate

    @property
    def time(self):
        r"""Gets the time of this GeneralRequest.

        :return: The time of this GeneralRequest.
        :rtype: :class:`huaweicloudsdkdbss.v1.Duration`
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this GeneralRequest.

        :param time: The time of this GeneralRequest.
        :type time: :class:`huaweicloudsdkdbss.v1.Duration`
        """
        self._time = time

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
        if not isinstance(other, GeneralRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

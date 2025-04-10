# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskOutputObs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket': 'str',
        'path': 'str',
        'data_category': 'list[str]'
    }

    attribute_map = {
        'bucket': 'bucket',
        'path': 'path',
        'data_category': 'data_category'
    }

    def __init__(self, bucket=None, path=None, data_category=None):
        r"""TaskOutputObs

        The model defined in huaweicloud sdk

        :param bucket: OBS桶名
        :type bucket: str
        :param path: OBS的路径
        :type path: str
        :param data_category: 作业输出数据类别的列表，当输出类型下有这个列表时，表示希望这个输出类型下存放dataCategory列表内的数据，部分服务需要
        :type data_category: list[str]
        """
        
        

        self._bucket = None
        self._path = None
        self._data_category = None
        self.discriminator = None

        self.bucket = bucket
        self.path = path
        if data_category is not None:
            self.data_category = data_category

    @property
    def bucket(self):
        r"""Gets the bucket of this TaskOutputObs.

        OBS桶名

        :return: The bucket of this TaskOutputObs.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this TaskOutputObs.

        OBS桶名

        :param bucket: The bucket of this TaskOutputObs.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def path(self):
        r"""Gets the path of this TaskOutputObs.

        OBS的路径

        :return: The path of this TaskOutputObs.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this TaskOutputObs.

        OBS的路径

        :param path: The path of this TaskOutputObs.
        :type path: str
        """
        self._path = path

    @property
    def data_category(self):
        r"""Gets the data_category of this TaskOutputObs.

        作业输出数据类别的列表，当输出类型下有这个列表时，表示希望这个输出类型下存放dataCategory列表内的数据，部分服务需要

        :return: The data_category of this TaskOutputObs.
        :rtype: list[str]
        """
        return self._data_category

    @data_category.setter
    def data_category(self, data_category):
        r"""Sets the data_category of this TaskOutputObs.

        作业输出数据类别的列表，当输出类型下有这个列表时，表示希望这个输出类型下存放dataCategory列表内的数据，部分服务需要

        :param data_category: The data_category of this TaskOutputObs.
        :type data_category: list[str]
        """
        self._data_category = data_category

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
        if not isinstance(other, TaskOutputObs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

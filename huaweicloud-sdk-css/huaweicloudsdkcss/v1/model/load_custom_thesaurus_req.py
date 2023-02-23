# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoadCustomThesaurusReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket_name': 'str',
        'main_object': 'str',
        'stop_object': 'str',
        'synonym_object': 'str'
    }

    attribute_map = {
        'bucket_name': 'bucketName',
        'main_object': 'mainObject',
        'stop_object': 'stopObject',
        'synonym_object': 'synonymObject'
    }

    def __init__(self, bucket_name=None, main_object=None, stop_object=None, synonym_object=None):
        """LoadCustomThesaurusReq

        The model defined in huaweicloud sdk

        :param bucket_name: 词库文件存放的OBS桶（桶类型必须为标准存储或者低频存储，不支持归档存储）。
        :type bucket_name: str
        :param main_object: 主词库文件对象，必须为UTF-8无BOM编码的文本文件，一行一个分词，文件大小最大支持100M。 mainObject, stopObject, synonymObject三个参数至少要填写一个。  &gt;一次只能加载一个主词库，不支持同时加载多个主词库。
        :type main_object: str
        :param stop_object: 停词词库文件对象，必须为UTF-8无BOM编码的文本文件，一行一个分词，文件大小最大支持20M。  mainObject, stopObject, synonymObject三个参数至少要填写一个。
        :type stop_object: str
        :param synonym_object: 同义词词库文件，必须为UTF-8无BOM编码的文本文件，一行一组分词，文件大小最大支持20M。  mainObject, stopObject, synonymObject三个参数至少要填写一个。
        :type synonym_object: str
        """
        
        

        self._bucket_name = None
        self._main_object = None
        self._stop_object = None
        self._synonym_object = None
        self.discriminator = None

        self.bucket_name = bucket_name
        if main_object is not None:
            self.main_object = main_object
        if stop_object is not None:
            self.stop_object = stop_object
        if synonym_object is not None:
            self.synonym_object = synonym_object

    @property
    def bucket_name(self):
        """Gets the bucket_name of this LoadCustomThesaurusReq.

        词库文件存放的OBS桶（桶类型必须为标准存储或者低频存储，不支持归档存储）。

        :return: The bucket_name of this LoadCustomThesaurusReq.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this LoadCustomThesaurusReq.

        词库文件存放的OBS桶（桶类型必须为标准存储或者低频存储，不支持归档存储）。

        :param bucket_name: The bucket_name of this LoadCustomThesaurusReq.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def main_object(self):
        """Gets the main_object of this LoadCustomThesaurusReq.

        主词库文件对象，必须为UTF-8无BOM编码的文本文件，一行一个分词，文件大小最大支持100M。 mainObject, stopObject, synonymObject三个参数至少要填写一个。  >一次只能加载一个主词库，不支持同时加载多个主词库。

        :return: The main_object of this LoadCustomThesaurusReq.
        :rtype: str
        """
        return self._main_object

    @main_object.setter
    def main_object(self, main_object):
        """Sets the main_object of this LoadCustomThesaurusReq.

        主词库文件对象，必须为UTF-8无BOM编码的文本文件，一行一个分词，文件大小最大支持100M。 mainObject, stopObject, synonymObject三个参数至少要填写一个。  >一次只能加载一个主词库，不支持同时加载多个主词库。

        :param main_object: The main_object of this LoadCustomThesaurusReq.
        :type main_object: str
        """
        self._main_object = main_object

    @property
    def stop_object(self):
        """Gets the stop_object of this LoadCustomThesaurusReq.

        停词词库文件对象，必须为UTF-8无BOM编码的文本文件，一行一个分词，文件大小最大支持20M。  mainObject, stopObject, synonymObject三个参数至少要填写一个。

        :return: The stop_object of this LoadCustomThesaurusReq.
        :rtype: str
        """
        return self._stop_object

    @stop_object.setter
    def stop_object(self, stop_object):
        """Sets the stop_object of this LoadCustomThesaurusReq.

        停词词库文件对象，必须为UTF-8无BOM编码的文本文件，一行一个分词，文件大小最大支持20M。  mainObject, stopObject, synonymObject三个参数至少要填写一个。

        :param stop_object: The stop_object of this LoadCustomThesaurusReq.
        :type stop_object: str
        """
        self._stop_object = stop_object

    @property
    def synonym_object(self):
        """Gets the synonym_object of this LoadCustomThesaurusReq.

        同义词词库文件，必须为UTF-8无BOM编码的文本文件，一行一组分词，文件大小最大支持20M。  mainObject, stopObject, synonymObject三个参数至少要填写一个。

        :return: The synonym_object of this LoadCustomThesaurusReq.
        :rtype: str
        """
        return self._synonym_object

    @synonym_object.setter
    def synonym_object(self, synonym_object):
        """Sets the synonym_object of this LoadCustomThesaurusReq.

        同义词词库文件，必须为UTF-8无BOM编码的文本文件，一行一组分词，文件大小最大支持20M。  mainObject, stopObject, synonymObject三个参数至少要填写一个。

        :param synonym_object: The synonym_object of this LoadCustomThesaurusReq.
        :type synonym_object: str
        """
        self._synonym_object = synonym_object

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
        if not isinstance(other, LoadCustomThesaurusReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
